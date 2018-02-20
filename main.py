"""Copyright (c) 2018 * Keith Cestaro
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


end = "/end"


def main():
    userInput = ""
    print("Hello, what is on your mind?")
    while userInput != end:
        userInput = str(input()).lower()
        print(searchInput(userInput))


def searchInput(ui):
    i = 0
    while i < len(ui):
        if ui == "/end":
            return ""
        if ui[i] == "a":
            if ui[i:(i + 5)] == "apple":
                return "An apple a day keeps the doctor away!"
        if ui[i] == "b":
            if ui[i:(i + 11)] == "burger king":
                return "I love some BK!"
        if ui[i] == "m":
            if ui[i:(i + 3)] == "mad":
                return "Relax, life is hard!"
        if ui[i] == "s":
            if ui[i:(i + 3)] == "sad":
                return "Aw! Cheer up!"
        i += 1
    return "I see"

main()