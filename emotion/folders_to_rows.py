from pathlib import Path
import uuid


template = """
<td>
    <div id="{id}"></div>
    <button id="{button_id}" class="play-button-demo btn btn-primary" onclick="{var}.playPause()"> <i class="fa fa-play"></i> Play / <i class="fa fa-pause"></i> Pause </button>
    <script> var {var} = WaveSurfer.create({{ container: '#{id}', waveColor: 'violet', progressColor: 'purple' }});
        {var}.load('{wav_path}'); </script>
</td>
"""
root = Path("./audio/same_sentence/female_1")

wavs = root.glob("*.wav")
out = ""

for wav in wavs:
    uid = "X" + uuid.uuid4().hex.upper()[0:6]
    button_uid = "X" + uuid.uuid4().hex.upper()[0:6]
    var_uid = "X" + uuid.uuid4().hex.upper()[0:6]
    out += template.format(id=uid, var=var_uid, button_id=button_uid, wav_path=str(wav)) + "\n"
print(out)
