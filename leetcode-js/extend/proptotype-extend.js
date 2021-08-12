/**
 * 父类作为子类原型
 */
function Parent() {
    this.name = 'father';
    this.nation = 'China';
}
Parent.prototype.say = function() { console.log('hello world') }

function Child(like) {
    this.like = like;
}
Child.prototype = new Parent();

let boy = new Child();

/**
 * 优点：1、构造函数方法可以共享
 * 缺点：1、子类修改共享属性会互相污染 2、不能传参数
 */