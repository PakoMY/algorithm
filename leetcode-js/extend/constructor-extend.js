/**
 * 借用父类的构造函数增强子类
 * @param {*} name 
 */
function Parent(name) {
    this.name = name;
    this.nation = 'China';
    this.say = function() { console.log('hello world') }
}

function Child(name, like) {
    Parent.call(this, name);
    this.like = like;
}

let boy = new Child('Tom','apple');
/**
 * 优点：1、可传参 2、不共享引用属性（nation属性）
 * 缺点：1、父类方法不能复用
 */