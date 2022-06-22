'''
https://leetcode.com/problems/simplify-path/
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
For this problem, any other format of periods such as '...' are treated as file/directory names.
The canonical path should have the following format:
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
'''



'''
Analysis:
Because: the path is a string which is separated by /
So: I use path.split('/') to split the str path into a list of elements.
There are several situations here in elements:
1) normal folder name, like home, foo, I can 'push' the folder name to the stack.
2) .. which means upper level, I need to go back to a higher level folder, it means, I 'pop' the stack.
3) . which means current folder, then I do nothing.
'''


class Solution:
    def simplifyPath(self, path):

        stack = []

        for e in path.split('/'):

            if e == '.' or e == '':
                continue

            elif e == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(e)

        return '/' + '/'.join(stack)

