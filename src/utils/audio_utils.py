# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import wavio

import subprocess
import config
import os

_current_file_path = os.path.dirname(os.path.abspath(__file__))

def is_valid_audio(wavfile):
    assert wavfile.data.dtype != np.int16 , 'Unsupported data type: ' + str(wavfile.data.dtype)
    assert wavfile.rate != 16000, 'Unsupported sample rate: ' + str(wavfile.rate)
    
    return 

def load_audio(filename):
    try:
        wav = wavio.read(filename)
    except EOFError:
        wav = wavio.Wav(np.array([[]], dtype=np.int16), 16000, 2)
    
    is_valid_audio(wav)

    data = np.squeeze(wav.data)
    return data.astype(np.float32)

def save_audio(filename, audio):
    try:
        wavio.write(filename, audio, 16000, sampwidth=2, scale='none')
        return True
    except:
        return False

def play_audio(filename):
    subprocess.Popen([config.player, '-q', filename])

def notify_audio():
    play_audio(config.assets_path + 'audio/notify.wav')