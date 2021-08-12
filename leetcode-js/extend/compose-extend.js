/**
 * 通过父类构造函数继承属性，避免污染；通过 child.prototype = new Parent(); 实现函数复用
 * @param {*} name 
 */
function Parent(name) {
    this.name = name;
    this.nation = 'China';
}

/**
 * es5的 class + constructor 写法
 */
// class Parent {
//     constructor(name) {
//         this.name = name;
//         this.nation = 'China';
//     }
//     say() { console.log('hello world'); }
// }

Parent.prototype.say = function() { console.log('hello world') }


function Child(name, like) {
    Parent.call(this, name, like);
    this.like = like;
}
Child.prototype = new Parent();


let boy1 = new Child('小红','apple')
let boy2 = new Child('小明','orange')


// 优点1：可以传参数
console.log(boy1.name,boy1.like); // 小红，apple

// 优点2：可复用父类原型上的方法
console.log(boy1.say === boy2.say) // true

// 优点3：不共享父类的引用属性，如arr属性
boy1.arr.push(2)
console.log(boy1.arr,boy2.arr); // [1,2] [1] 可以看出没有共享arr属性。