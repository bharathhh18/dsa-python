#Infix to Postfix Conversion
class solution:
    def precedence(self,ch):
        if ch=="^":
            return 3
        elif ch=="*" or ch=="/":
            return 2
        elif ch=="+" or ch=="-":
            return 1
        return 0

    def infixToPostfix(self,exp):
        stack=[]
        result=[]
        for char in exp:
            if ('a'<=char<='z') or ('A'<=char<='Z') or ('0'<=char<='9'):
                result.append(char)
            elif char=='(':
                stack.append(char)
            elif char==')':
                while stack and stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(char)<=self.precedence(stack[-1]):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result)
ans=solution()
print(ans.infixToPostfix("(A+B)*(C-D)"))

# Infix to Prefix Conversion
#first reverse the infix expression
#change ')' to '(' and '(' to ')'
#reverse the postfix expression to get prefix expression
class solution:
    def precedence(self,ch):
        if ch=="^":
            return 3
        elif ch=="*" or ch=="/":
            return 2
        elif ch=="+" or ch=="-":
            return 1
        return 0

    def infixToPostfix(self,exp):
        stack=[]
        result=[]
        exp=exp[::-1]
        exp=exp.replace('(','temp').replace(')','(').replace('temp',')')
        for char in exp:
            if ('a'<=char<='z') or ('A'<=char<='Z') or ('0'<=char<='9'):
                result.append(char)
            elif char=='(':
                stack.append(char)
            elif char==')':
                while stack and stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(char)<self.precedence(stack[-1]):
                    result.append(stack.pop())
                stack.append(char)
        while stack:
            result.append(stack.pop())
        return "".join(result[::-1])
ans=solution()
print(ans.infixToPostfix("(A+B)*(C-D)"))