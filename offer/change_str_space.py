


str1 = "we are happy"


class Solution:
    def switch1(self, s):
        return s.replace(' ', '%20')

    def switch2(self, s):
        return "%20".join(s.split(' '))

    def switch3(self, s):
        new_s = ""
        for i in s:
            if i == ' ':
                new_s += "%20"
            else:
                new_s += i
        return new_s

    def switch4(self, s):
        num_space = 0
        for i in s:
            if i == " ":
                num_space += 1

        old_length = len(s)
        new_length = len(s) + 2 * num_space
        old_index = old_length - 1
        new_index = new_length - 1
        new_string = [0 for _ in range(new_length)]
        for i in s[::-1]:
            if i == " ":
                new_string[new_index] = "0"
                new_index -= 1
                new_string[new_index] = "2"
                new_index -= 1
                new_string[new_index] = "%"
            else:
                new_string[new_index] = s[old_index]
            new_index -= 1
            old_index -= 1
        return ''.join(new_string)



s = Solution()
print(s.switch1(str1))
print(s.switch2(str1))
print(s.switch3(str1))
print(s.switch4(str1))
