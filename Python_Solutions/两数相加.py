from LinkedList import LinkedList,ListNode
class Solution:
    def addTwoNumbers(self, num1, num2):
        carry = 0
        head = cur = ListNode(0)
        while num1 or num2 or carry:
            if num1:
                cur.val = cur.val + int(num1.val)
                num1 = num1.next
            if num2:
                cur.val = cur.val + int(num2.val)
                num2 = num2.next
            if carry:
                cur.val = cur.val + carry
            carry = cur.val//10
            cur.val = cur.val%10
            cur.next = ListNode(0)
            cur = cur.next
        return head
num1 = LinkedList().create(['7','8','9'])
num2 = LinkedList().create(['2','8','9'])
result = Solution().addTwoNumbers(num1,num2)
while result:
    print(result.val)
    result = result.next