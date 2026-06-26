$text = [IO.File]::ReadAllText('C:\Users\henrique\.gemini\antigravity\brain\e75f1c7b-fd54-4b6f-9e7d-95bfdd66390f\.system_generated\steps\5\content.md', [System.Text.Encoding]::UTF8);
$start = $text.IndexOf('<!DOCTYPE html>');
$html = $text.Substring($start);
$html = $html.Replace('="imagens/', '="https://kitconsultorioludico.vercel.app/imagens/');
[IO.File]::WriteAllText('c:\Users\henrique\Downloads\consultorio\index.html', $html, [System.Text.Encoding]::UTF8);
