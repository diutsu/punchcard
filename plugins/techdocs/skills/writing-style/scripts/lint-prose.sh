#!/bin/sh
# Usage: lint-prose.sh <file>...
# Greps each file for banned words, phrases, placeholders and chatbot/citation residue.
# Prints "file:line: pattern" per hit. Exit 1 when any hit exists, 0 when clean.

if [ "$#" -eq 0 ]; then
  echo "usage: lint-prose.sh <file>..." >&2
  exit 2
fi

# Whole-word or phrase patterns, matched case-insensitively.
WORDS='delve|delving|tapestry|leverage|leveraging|robust|seamless|seamlessly|comprehensive|crucial|pivotal|meticulous|meticulously|intricate|underscore|underscores|showcase|showcases|foster|fosters|fostering|enhance|enhances|multifaceted|utilize|utilizes|testament|landscape|vibrant|enduring|interplay|bolster|bolstered|garner|boasts|valuable insights|in order to|it should be noted|it is important to note|it.s important to note|basically|essentially|in conclusion|in summary|to summarize|stands as|serves as|a testament to|plays a pivotal role|indelible mark|key turning point|not just|not only|experts say|experts argue|industry reports|observers have|studies show|i hope this helps|let me know if|as an ai|as a language model|great question|knowledge cutoff|\[insert|utm_|oaicite|contentreference|turn0search|nestled|in the heart of|breathtaking|groundbreaking|diverse array|rich tapestry|deep dive|despite these challenges|faces several challenges|future outlook|challenges and legacy|setting the stage for|focal point|deeply rooted|evolving landscape|maintains an? (strong|active) (digital|social media) presence|independent coverage|does not by itself establish|not widely documented|based on available information|in the provided sources|should not be confused|as of my last (knowledge|training) update|as a large language model|would you like|is there anything else|you.re absolutely right|ensured that|while preserving'

# Placeholder and residue patterns that end in punctuation, so no word boundary.
RAW='\[(your|insert|describe|brief|year|date|link)[^]]*\]|insert_[a-z_]*url[a-z_0-9]*|paste_[a-z_]*_here|example\.com/[a-z]+[0-9]*|[0-9]{4}-(xx|[0-9]{2})-xx|referrer=grok|(of course|certainly)!|\*\*[^*]+\*\*:'

status=0
for f in "$@"; do
  if [ ! -f "$f" ]; then
    echo "$f: not a file" >&2
    status=2
    continue
  fi
  out=$(grep -n -i -o -E "\b($WORDS)\b|\[insert|utm_[a-z]+|$RAW" "$f" | sed "s|^\([0-9]*\):\(.*\)|$f:\1: \2|")
  if [ -n "$out" ]; then
    printf '%s\n' "$out"
    [ "$status" -eq 0 ] && status=1
  fi
done
exit "$status"
