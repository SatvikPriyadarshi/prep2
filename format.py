import sys

def format_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    i = 0
    
    in_question = False
    q_num = ""
    q_text = ""
    options = []
    answer = ""
    explanation = ""
    
    def emit_question():
        nonlocal in_question, q_num, q_text, options, answer, explanation
        if in_question:
            out.append(f"\n### {q_num} {q_text.strip()}\n")
            for opt in options:
                out.append(f"- {opt.strip()}\n")
            out.append("\n<details>\n<summary><b>View Answer & Explanation</b></summary>\n\n")
            out.append(f"> **Answer:** {answer.strip()}  \n")
            out.append(f"> **Explanation:** {explanation.strip()}\n\n")
            out.append("</details>\n")
            
            in_question = False
            q_num = ""
            q_text = ""
            options = []
            answer = ""
            explanation = ""

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if stripped.startswith("Topic ") or stripped.startswith("📘 Topic "):
            s = stripped.replace("📘 ", "")
            out.append(f"# {s}\n\n")
        elif stripped.startswith("📝 Quick Revision Cheat Sheet"):
            out.append("## 📝 Quick Revision Cheat Sheet (Before you start)\n\n")
        elif stripped.startswith("Part ") and "(Questions" in stripped:
            emit_question()
            out.append(f"\n## {stripped}\n\n")
        elif stripped.startswith("**") and stripped[2].isdigit() or (stripped and stripped[0].isdigit() and ". " in stripped[:10]):
            emit_question()
            in_question = True
            s = stripped.replace("**", "")
            parts = s.split(". ", 1)
            if len(parts) == 2:
                q_num = parts[0] + "."
                q_text = parts[1]
            else:
                q_num = parts[0]
                q_text = ""
        elif in_question:
            if stripped.startswith("A)") or stripped.startswith("B)") or stripped.startswith("C)") or stripped.startswith("D)"):
                options.append(stripped)
            elif stripped.startswith("Answer:"):
                answer = stripped.split("Answer:", 1)[1]
            elif stripped.startswith("Explanation:"):
                explanation = stripped.split("Explanation:", 1)[1]
                j = i + 1
                while j < len(lines):
                    next_stripped = lines[j].strip()
                    if next_stripped == "" or next_stripped.startswith("Part ") or (next_stripped and next_stripped[0].isdigit() and ". " in next_stripped[:10]) or next_stripped.startswith("**"):
                        break
                    explanation += " " + next_stripped
                    j += 1
                i = j - 1
            elif not stripped:
                pass
            else:
                if not options and not answer and not explanation:
                    q_text += " " + stripped
        else:
            if ":" in stripped and not stripped.startswith("#") and not stripped.startswith("Part") and not stripped.startswith("Topic "):
                parts = stripped.split(":", 1)
                out.append(f"- **{parts[0].strip()}:** {parts[1].strip()}\n")
            elif stripped:
                out.append(f"{stripped}\n")
        
        i += 1
        
    emit_question()
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(out)

if __name__ == "__main__":
    format_file(sys.argv[1])
