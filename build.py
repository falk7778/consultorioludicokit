import sys

with open(r'C:\Users\henrique\.gemini\antigravity\brain\996b601b-d156-41d3-8e88-a6eb84a3e2aa\.system_generated\steps\4\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<!DOCTYPE html>')
if start >= 0:
    html = content[start:]
    html = html.replace('src="imagens/', 'src="https://kitconsultorioludico.vercel.app/imagens/')
    html = html.replace('href="imagens/', 'href="https://kitconsultorioludico.vercel.app/imagens/')
    
    with open(r'c:\Users\henrique\Downloads\consultorio\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Failed")
