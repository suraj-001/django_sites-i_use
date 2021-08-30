#i have added this file
from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1>Suraj</h1> <li> <a href="https://www.udemy.com/course/git-github-practical-guide/learn/lecture/28082510#overview">UDEmy Github</a></li>
    <li> <a href="https://leetcode.com/problemset/all/">Leetcode</a></li>
    <li> <a href="https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/">GFG must do</a></li>
''')
def about(request):
    return HttpResponse("<h1> about hello </h1>")