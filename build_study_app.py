"""Build clf_c02_study_app.html from content modules."""
import json
import random
import re

from exam_content import LESSONS as BASE_LESSONS, QUESTIONS as BASE_QUESTIONS
from extra_questions import EXTRA_QUESTIONS
from lesson_enrichment import LESSON_ENRICH
from flashcards_data import FLASHCARDS

random.seed(42)  # even answer distribution at rest; runtime shuffle still randomizes


def merge_lessons():
    lessons = []
    for L in BASE_LESSONS:
        lid = L["id"]
        e = LESSON_ENRICH.get(lid, {})
        points = list(L.get("points", []))
        points.extend(e.get("extra_points", []))
        lessons.append({
            "id": lid,
            "d": L["d"],
            "title": L["title"],
            "icon": L.get("icon", "ti-book"),
            "points": points,
            "comparisons": e.get("comparisons", []),
            "traps": e.get("traps", []),
        })
    return lessons


def shuffle_question_opts(q):
    """Shuffle options and remap answer indices for even distribution at rest."""
    q = dict(q)
    n = len(q["opts"])
    perm = list(range(n))
    random.shuffle(perm)
    inv = {old: new for new, old in enumerate(perm)}
    q["opts"] = [q["opts"][i] for i in perm]
    if q.get("multi"):
        q["a"] = sorted(inv[i] for i in q["a"])
    else:
        q["a"] = inv[q["a"]]
    return q


def build_questions():
    all_q = BASE_QUESTIONS + EXTRA_QUESTIONS
    out = []
    for i, q in enumerate(all_q):
        q = dict(q)
        q["id"] = f"{q['t']}-{i:04d}"
        out.append(shuffle_question_opts(q))
    return out


SHUFFLE_JS = r'''
function shuffleArray(arr){
  const a=arr.slice();
  for(let i=a.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    const t=a[i];a[i]=a[j];a[j]=t;
  }
  return a;
}

function prepareQuestion(q){
  const clone=JSON.parse(JSON.stringify(q));
  const n=clone.opts.length;
  const perm=shuffleArray(Array.from({length:n},(_,i)=>i));
  const inv={};
  perm.forEach((oldIdx,newIdx)=>{inv[oldIdx]=newIdx;});
  clone.opts=perm.map(i=>q.opts[i]);
  if(isMulti(clone)){
    clone.a=clone.a.map(i=>inv[i]).sort((a,b)=>a-b);
  }else{
    clone.a=inv[clone.a];
  }
  clone._bankId=q.id||q.t;
  return clone;
}

function prepareSession(questions){
  return shuffleArray(questions.map(prepareQuestion));
}

function findBankIndex(q){
  if(q.id)return QUESTION_BANK.findIndex(b=>b.id===q.id);
  if(q._bankId)return QUESTION_BANK.findIndex(b=>b.id===q._bankId);
  return QUESTION_BANK.findIndex(b=>b.t===q.t&&b.q===q.q);
}
'''

LESSON_HTML_PATCH = '''      <div class="lesson-body">
        <div class="lesson-section-title">📚 What you need to know</div>
        <ul id="lesson-points"></ul>
      </div>
      <div class="lesson-comparisons" id="lesson-comparisons-wrap" style="display:none">
        <div class="lesson-section-title">⚖️ Service comparisons (exam favorites)</div>
        <div id="lesson-comparisons"></div>
      </div>
      <div class="lesson-traps" id="lesson-traps-wrap" style="display:none">
        <div class="lesson-section-title">⚠️ Exam traps — don't fall for these!</div>
        <ul id="lesson-traps"></ul>
      </div>'''

LESSON_CSS = '''
.lesson-section-title{font-size:13px;font-weight:600;color:var(--accent);margin-bottom:10px}
.lesson-comparisons,.lesson-traps{background:var(--color-background-secondary);border:1px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:1.25rem 1.5rem;margin-bottom:1.25rem}
.lesson-traps ul{list-style:none;padding:0}
.lesson-traps li{padding:8px 0;border-bottom:1px solid var(--color-border-tertiary);font-size:13px;line-height:1.55;color:var(--warn)}
.lesson-traps li:last-child{border-bottom:none}
.comparison-card{padding:10px 0;border-bottom:1px solid var(--color-border-tertiary)}
.comparison-card:last-child{border-bottom:none;padding-bottom:0}
.comparison-card h4{font-size:13px;font-weight:600;color:var(--color-text-primary);margin-bottom:4px}
.comparison-card p{font-size:13px;color:var(--color-text-secondary);line-height:1.55}
'''


def patch_open_lesson(js):
    old = """  document.getElementById('lesson-points').innerHTML=lesson.points.map(p=>'<li>'+p+'</li>').join('');
}"""
    new = """  document.getElementById('lesson-points').innerHTML=lesson.points.map(p=>'<li>'+p+'</li>').join('');
  const cmpWrap=document.getElementById('lesson-comparisons-wrap');
  const cmpEl=document.getElementById('lesson-comparisons');
  if(lesson.comparisons&&lesson.comparisons.length){
    cmpWrap.style.display='block';
    cmpEl.innerHTML=lesson.comparisons.map(c=>'<div class="comparison-card"><h4>'+c.title+'</h4><p>'+c.text+'</p></div>').join('');
  }else{cmpWrap.style.display='none';}
  const trapWrap=document.getElementById('lesson-traps-wrap');
  const trapEl=document.getElementById('lesson-traps');
  if(lesson.traps&&lesson.traps.length){
    trapWrap.style.display='block';
    trapEl.innerHTML=lesson.traps.map(t=>'<li>'+t+'</li>').join('');
  }else{trapWrap.style.display='none';}
}"""
    if old in js:
        return js.replace(old, new)
    return js


def patch_session_starts(js):
    # startLessonQuiz
    js = js.replace(
        "function startLessonQuiz(){\n  const qs=QUESTION_BANK.filter(q=>q.t===learnSession.lessonId);\n  learnSession={lessonId:learnSession.lessonId,questions:qs,answers:new Array(qs.length).fill(null),current:0,multiDraft:[]};",
        "function startLessonQuiz(){\n  const pool=QUESTION_BANK.filter(q=>q.t===learnSession.lessonId);\n  const qs=prepareSession(pool);\n  learnSession={lessonId:learnSession.lessonId,questions:qs,answers:new Array(qs.length).fill(null),current:0,multiDraft:[]};",
    )
    # buildSession
    js = js.replace(
        "  pool=pool.sort(()=>Math.random()-0.5).slice(0,Math.min(count,pool.length));\n  currentSession={",
        "  pool=prepareSession(pool).slice(0,Math.min(count,pool.length));\n  currentSession={",
    )
    # startReadinessCheck
    js = js.replace(
        "  currentSession={questions:pool.sort(()=>Math.random()-0.5),answers:new Array(pool.length).fill(null)",
        "  currentSession={questions:prepareSession(pool),answers:new Array(pool.length).fill(null)",
    )
    # weak spots filter - use id
    js = js.replace(
        "if(domain==='weak')pool=pool.filter(q=>globalStats.wrongIds.includes(QUESTION_BANK.indexOf(q)));",
        "if(domain==='weak')pool=pool.filter(q=>globalStats.wrongIds.includes(q.id));",
    )
    # recordAnswer wrong id
    js = js.replace(
        "  const qIdx=QUESTION_BANK.indexOf(q);\n  globalStats.attempted++;\n  if(isCorrect(q,ans)){globalStats.correct++;globalStats.streak++;}\n  else{globalStats.streak=0;if(qIdx>=0&&!globalStats.wrongIds.includes(qIdx))globalStats.wrongIds.push(qIdx);}",
        "  const qId=q.id||q._bankId;\n  globalStats.attempted++;\n  if(isCorrect(q,ans)){globalStats.correct++;globalStats.streak++;}\n  else{globalStats.streak=0;if(qId&&!globalStats.wrongIds.includes(qId))globalStats.wrongIds.push(qId);}",
    )
    js = js.replace(
        "if(domain==='weak')pool=pool.filter(q=>globalStats.wrongIds.includes(q.id));",
        "if(domain==='weak')pool=QUESTION_BANK.filter(q=>globalStats.wrongIds.includes(q.id));",
    )
    return js


def main():
    lessons = merge_lessons()
    questions = build_questions()
    multi = sum(1 for q in questions if q.get("multi"))

    with open("clf_c02_study_app.html", "r", encoding="utf-8") as f:
        html = f.read()

    # CSS
    if ".lesson-comparisons" not in html:
        html = html.replace(".hero-cta{", LESSON_CSS + "\n.hero-cta{")

    # Lesson HTML structure
    html = html.replace(
        '<div class="lesson-body"><ul id="lesson-points"></ul></div>',
        LESSON_HTML_PATCH,
    )
    html = html.replace(
        "~2 min lesson",
        "~8 min lesson",
    )
    html = html.replace(
        "short mini-lesson",
        "full mini-lesson with exam traps",
    )

    # Replace data
    html = re.sub(
        r"const LESSONS = \[.*?\];\n\n",
        "const LESSONS = " + json.dumps(lessons, ensure_ascii=False) + ";\n\n",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r"const QUESTION_BANK = \[.*?\];\n",
        "const QUESTION_BANK = " + json.dumps(questions, ensure_ascii=False) + ";\n",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r"const FC_TERMS = \[.*?\];\n",
        "const FC_TERMS = " + json.dumps(FLASHCARDS, ensure_ascii=False) + ";\n",
        html,
        count=1,
        flags=re.S,
    )

    # Inject shuffle JS after multiLabel function
    if "function prepareQuestion" not in html:
        html = html.replace(
            "function multiLabel(q){",
            SHUFFLE_JS + "\nfunction multiLabel(q){",
        )

    # Extract script and patch functions
    script_m = re.search(r"<script>\n(.*)\n</script>\n</body>", html, re.S)
    if script_m:
        js = script_m.group(1)
        js = patch_open_lesson(js)
        js = patch_session_starts(js)
        html = html[: script_m.start(1)] + js + html[script_m.end(1) :]

    with open("clf_c02_study_app.html", "w", encoding="utf-8") as f:
        f.write(html)

    from collections import Counter
    dist = Counter(q["a"] for q in questions if not q.get("multi"))
    print(f"Built: {len(questions)} questions ({multi} multi-select)")
    print(f"Lessons: {len(lessons)}, Flashcards: {len(FLASHCARDS)}")
    print(f"Answer distribution (at rest): {dict(sorted(dist.items()))}")


if __name__ == "__main__":
    main()
