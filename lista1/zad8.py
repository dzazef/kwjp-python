import re


class RzymArabException(Exception):
    pass


class RzymToArab:
    rzym_arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rzym_pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    def translate(self, s):
        pattern = re.compile(self.rzym_pattern)
        if pattern.match(s) is None:
            raise RzymArabException()

        value = self.rzym_arab[s[0]]
        for i in range(1, len(s)):
            if self.rzym_arab[s[i]] > self.rzym_arab[s[i - 1]]:
                value += self.rzym_arab[s[i]] - 2 * self.rzym_arab[s[i - 1]]
            else:
                value += self.rzym_arab[s[i]]
        return value


print(RzymToArab().translate('CMXXXIV'))
