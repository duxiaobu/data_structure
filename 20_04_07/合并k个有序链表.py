from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        """
        暴力法，把所有节点值保存金数组中，排序后再组装新的链表
        时间复杂度：O(nlogn)
        空间复杂度：O(n)
        :param lists:
        :return:
        """
        self.arr = []
        # 全部加入到数组中
        for link_list in lists:
            while link_list:
                self.arr.append(link_list.val)
                link_list = link_list.next
        # 排序后，重新生成链表
        head = cur_node = ListNode(0)
        for item in sorted(self.arr):
            cur_node.next = ListNode(item)
            cur_node = cur_node.next
        return head.next

    def mergeKLists2(self, lists: [ListNode]) -> ListNode:
        """
        使用优先队列，优先队列底层就是堆实现的
        时间复杂度：O(nlogk)
        空间复杂度：O(n)
        :param lists:
        :return:
        """
        q = PriorityQueue()
        head = cur_node = ListNode(0)
        for index, l in enumerate(lists):
            if l:
                q.put((l.val, index))
        while not q.empty():
            value, index = q.get()
            cur_node.next = lists[index]
            cur_node = cur_node.next
            lists[index] = lists[index].next
            if lists[index]:
                q.put((lists[index].val, index))
        return head.next

    def mergeKLists3(self, lists: [ListNode]) -> ListNode:
        length = len(lists)
        interval = 1
        while interval < length:
            for i in range(0, length - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if lists else lists

    def merge2Lists(self, l1, l2):
        head = cur_node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur_node.next, l1 = l1, l1.next
            else:
                cur_node.next, l2 = l2, l2.next
            cur_node = cur_node.next
        cur_node.next = l1 if l1 else l2
        return head.next


if __name__ == '__main__':
    for i in range(0, 4, 4):
        print(i)
