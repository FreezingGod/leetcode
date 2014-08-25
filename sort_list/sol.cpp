/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>
#include <stddef.h>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
ListNode* merge(ListNode *head1, ListNode *head2);

ListNode* sortList(ListNode* head) {
    if (head == NULL || head->next == NULL) 
        return head;
    ListNode *fast = head;
    ListNode *slow = head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    ListNode *head1 = head;
    ListNode *head2 = slow->next;
    slow->next = NULL;
    ListNode *h1 = sortList(head1);
    ListNode *h2 = sortList(head2);
    ListNode *rtn = merge(h1, h2);
    return rtn;
}

ListNode* merge(ListNode *head1, ListNode *head2) {
    if (head1 == NULL)
        return head2;
    if (head2 == NULL)
        return head1;
    ListNode *dummy = new ListNode(0);
    ListNode *last = dummy;
    while (head1 != NULL && head2 != NULL) {
        if (head1->val < head2->val) {
            last->next = head1;
            head1 = head1->next;
            last = last->next;
        } else {
            last->next = head2;
            head2 = head2->next;
            last = last->next;
        }
    }
    if (head1 == NULL)
        last->next = head2;
    if (head2 == NULL)
        last->next = head1;
    return dummy->next;
}

int main(int argc, char **argv) {
    ListNode *node1 = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    node2->next = node1;
    cout << node2->val << " " << node2->next->val << endl;
    ListNode* rtn = sortList(node2);
    cout << rtn->val << " " << rtn->next->val << endl;
    return 0;
}
