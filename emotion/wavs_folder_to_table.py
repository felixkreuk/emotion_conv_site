import uuid
import collections
from collections import defaultdict
import argparse
from pathlib import Path
import jinja2
from jinja2 import Template


def create_html(content):
    template = Template("""
    <html>
    <head><link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css"></head>
    <title>Samples</title>
    <body>
    <main>
    <p>
    <code>src</code> stands for the source recording, this is used for priming the LM.
    <code>gen</code> denotes the generated recording. This is is comprised of the source segment + a generated segment.
    Start by listening the <code>src</code>.
    </p>
    {{ content }}
    </main>
    </body>
    </html>
    """)
    return template.render(content=content)


def create_table(parsed_dir, title):
    template = Template("""
    <br><div class="content-title">{{ title }}</div><br>
    <table border="0" class="inlineTable">
        <tr>
            <th>Source</th>
            <th>Generated</th>
            <th>Target</th>
        </tr>

        {% for item in parsed_dir %}
        <tr>
            <td>
                <div id="{{ item['src_div_id'] }}"></div>
                <button id="{{ item['src_button_id'] }}" class="play-button-demo btn btn-primary" onclick="{{ item['src_var'] }}.playPause()"> <i class="fa fa-play"></i> Play / <i class="fa fa-pause"></i> Pause </button>
                <script> var {{ item['src_var'] }} = WaveSurfer.create({ container: '#{{ item["src_div_id"] }}', waveColor: 'violet', progressColor: 'purple' });
                    {{ item['src_var'] }}.load('{{ item["src_path"] }}'); </script>
            </td>
            <td>
                <div id="{{ item['gen_div_id'] }}"></div>
                <button id="{{ item['gen_button_id'] }}" class="play-button-demo btn btn-primary" onclick="{{ item['gen_var'] }}.playPause()"> <i class="fa fa-play"></i> Play / <i class="fa fa-pause"></i> Pause </button>
                <script> var {{ item['gen_var'] }} = WaveSurfer.create({ container: '#{{ item["gen_div_id"] }}', waveColor: 'violet', progressColor: 'purple' });
                    {{ item['gen_var'] }}.load('{{ item["gen_path"] }}'); </script>
            </td>
            <td>
                <div id="{{ item['tgt_div_id'] }}"></div>
                <button id="{{ item['tgt_button_id'] }}" class="play-button-demo btn btn-primary" onclick="{{ item['tgt_var'] }}.playPause()"> <i class="fa fa-play"></i> Play / <i class="fa fa-pause"></i> Pause </button>
                <script> var {{ item['tgt_var'] }} = WaveSurfer.create({ container: '#{{ item["tgt_div_id"] }}', waveColor: 'violet', progressColor: 'purple' });
                    {{ item['tgt_var'] }}.load('{{ item["tgt_path"] }}'); </script>
            </td>
        </tr>
        {% endfor %}
    </table>
    """)

    return template.render(parsed_dir=parsed_dir, title=title)


def wavs_to_table(path):
    if "-" not in path: return

    parsed_dir = []
    path = Path(path)
    wavs = path.glob("**/*.wav")
    title = path.name.split("-")
    title = [x.capitalize() for x in title]
    title = title[0] + " to " + title[1]
    parsed_dir += [{
        "src_path": "./audio/" + "/".join(str(path).split("/")[-2:]) + "/src.wav",
        "gen_path": "./audio/" + "/".join(str(path).split("/")[-2:]) + "/gen.wav",
        "tgt_path": "./audio/" + "/".join(str(path).split("/")[-2:]) + "/tgt.wav",
        "src_div_id": "x" + uuid.uuid4().hex.upper()[0:6],
        "gen_div_id": "x" + uuid.uuid4().hex.upper()[0:6],
        "tgt_div_id": "x" + uuid.uuid4().hex.upper()[0:6],
        "src_button_id": "x" + uuid.uuid4().hex.upper()[0:6],
        "gen_button_id": "x" + uuid.uuid4().hex.upper()[0:6],
        "tgt_button_id": "x" + uuid.uuid4().hex.upper()[0:6],
        "src_var": "x" + uuid.uuid4().hex.upper()[0:6],
        "gen_var": "x" + uuid.uuid4().hex.upper()[0:6],
        "tgt_var": "x" + uuid.uuid4().hex.upper()[0:6],
    }]
    return create_table(parsed_dir, title)


if __name__ == "__main__":
    for f in Path("/Users/felixkreuk/Desktop/non_neutral_source").glob("**"):
        print(wavs_to_table(str(f)))
    
