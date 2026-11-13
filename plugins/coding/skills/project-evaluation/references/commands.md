# Measurement recipes

Run from the repo root. Adapt paths and extensions to the project.

## Churn

```bash
git log --since="12 months ago" --format= --name-only -- . | sort | uniq -c | sort -rn | head -30
```

## Churn crossed with size

```bash
git log --since="12 months ago" --format= --name-only -- '*.py' '*.ts' '*.go' \
  | sort | uniq -c | sort -rn | head -50 \
  | while read n f; do [ -f "$f" ] && echo "$n changes  $(wc -l < "$f") lines  $f"; done
```

## Co-change (files that change together)

```bash
git log --since="12 months ago" --format='@%h' --name-only \
  | awk '/^@/{if(n>1&&n<=15)for(i=1;i<=n;i++)for(j=i+1;j<=n;j++)print f[i]" | "f[j]; n=0; next} NF{f[++n]=$0}' \
  | sort | uniq -c | sort -rn | head -30
```

Pairs in different modules with a high count signal change amplification. Commits touching more than 15 files are skipped as bulk edits.

## Dependency direction

```bash
grep -rnE "^(import|from) " src/<moduleA> | grep "<moduleB>"
```

Run it both ways for each module pair. Imports in both directions are a cycle.

## SDK leakage

```bash
grep -rln "<sdk-package>" src | grep -v "<wrapper-module>"
```

## Error-handling consistency

```bash
grep -rnE "except\s*(Exception)?\s*:|catch\s*\(.*\)\s*\{\s*\}|\|\|\s*(null|\[\]|\{\})" src | head -40
```

## Dead code candidates

Search each exported symbol for references outside its definition, then confirm with coverage output before calling it dead. Dynamic dispatch and reflection can hide real uses.
