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

import os
import fnmatch

_current_file_path = os.path.dirname(os.path.abspath(__file__))

def ls(directory, extension):    
    result = []
    for root, _ , filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, extension):
            result.append(os.path.join(root, filename))
    return result

def ls_wav(directory):
    return (ls(os.path.join(directory, 'wake_word'), '*.wav'),
            ls(os.path.join(directory, 'not_wake_word'), '*.wav'))
