# MIT License

# Copyright (c) 2025 Winkarst

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unicodedata

lower_to_upper = {}
upper_to_lower = {}

for codepoint in range(0x10FFFF + 1):
    char = chr(codepoint)

    if unicodedata.category(char)[0] == 'L':
        upper_char = char.upper()
        lower_char = char.lower()

        if upper_char != char and len(upper_char) == 1:
            lower_to_upper[codepoint] = ord(upper_char)

        if lower_char != char and len(lower_char) == 1:
            upper_to_lower[codepoint] = ord(lower_char)

lua_content = "local casingsUpperToLower = {\n"

for upper_codepoint, lower_codepoint in sorted(upper_to_lower.items()):
    lua_content += f'    [{upper_codepoint}] = {lower_codepoint},\n'

lua_content += """}

local casingsLowerToUpper = {
"""

for lower_codepoint, upper_codepoint in sorted(lower_to_upper.items()):
    lua_content += f'    [{lower_codepoint}] = {upper_codepoint},\n'

lua_content += "}"

with open('casings.lua', 'w', encoding='utf-8') as f:
    f.write(lua_content)
