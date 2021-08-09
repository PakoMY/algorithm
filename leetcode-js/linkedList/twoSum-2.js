/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 * 输入：l1 = [2,4,3], l2 = [5,6,4]
 * 输出：[7,0,8]
 * 解释：342 + 465 = 807. 
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var addTwoNumbers = function(l1, l2) {
    let tempBit = 0;
    let result = [];
    let lessLengthList = l1.length > l2.length ? l2 : l1;
    let longLengthList = l1.length > l2.length ? l1 : l2;
    for(i = 0; i < lessLengthList.length; i++) {
        result.push(((l1[i] + l2[i]) % 10) + tempBit);
        tempBit = (l1[i] + l2[i]) > 9 ? 1 : 0; 
    }
    for(j = lessLengthList.length; j < longLengthList.length; j++) {
        let ele = j === lessLengthList.length ? longLengthList[j] + tempBit : longLengthList[j];
        result.push(ele);
    }
    if(lessLengthList.length === longLengthList.length && tempBit === 1) result.push(1);
    return res;
};

/**
 * 链表实现
 */
var addTwoNumbers_listNode = function(l1, l2) {
    // 创建临时的链表
    let resNode = new ListNode(0);
    // 记录好相关的临时链表信息
    let res = resNode;
    // 记录是否进行进位运算
    let flag = 0;
    //当l1不为空或l2不为空或不需要进位时
    while(l1 || l2 || flag) {
        // 记录其相关的值
        let val1 = l1?l1.val:0;
        let val2 = l2?l2.val:0;
        let sum = val1 + val2 + flag;
        //判断是否需要进位
        flag = sum >= 10 ? 1 : 0;
        //链表所存储的元素只能为余数
        sum = sum % 10;
        //当相关的链表不为空时，则链表一次向下遍历
        if(l1) {
            l1 = l1.next;
        }
        if(l2) {
            l2 = l2.next;
        }
        //向临时创建的链表追加元素
        resNode.next = new ListNode(sum);
        resNode = resNode.next;
    }
    return res.next;
};

// addTwoNumbers([8, 2, 6], [3, 2, 1, 9]);
addTwoNumbers([2, 4, 3], [5, 6, 4]);