leetcode show [keyword]

Show question

Positionals:
  keyword  Show question by name or id  [string] [default: ""]

Options:
  -h, --help      Show help  [boolean]
  -c, --codeonly  Only show code template  [boolean] [default: false]
  -e, --editor    Open source code in editor  [string]
  -g, --gen       Generate source code  [boolean] [default: false]
  -l, --lang      Programming language of the source code  [string] [choices: "bash", "c", "cpp", "csharp", "golang", "java", "javascript", "kotlin", "mysql", "python", "python3", "ruby", "rust", "scala", "swift"] [default: "python3"]
  -o, --outdir    Where to save source code  [string] [default: "."]
  -q, --query     Filter questions by condition:
                  Uppercase means negative
                  e = easy     E = m+h
                  m = medium   M = e+h
                  h = hard     H = e+m
                  d = done     D = not done
                  l = locked   L = non locked
                  s = starred  S = not starred  [string] [default: ""]
  -t, --tag       Filter questions by tag  [array] [default: []]
  -x, --extra     Show extra question details in source code  [boolean] [default: false]

Examples:
  leetcode show 1              Show question 1
  leetcode show 1 -gx -l java  Show question 1 and generate Java code
  leetcode show 1 -gxe         Open generated code in editor

  leetcode show                Show random question
  leetcode show -q h           Show random hard question
  leetcode show -t google      Show random question from Google (require plugin)

Invalid values:
  Argument: l, Given: "sql", Choices: "bash", "c", "cpp", "csharp", "golang", "java", "javascript", "kotlin", "mysql", "python", "python3", "ruby", "rust", "scala", "swift"
