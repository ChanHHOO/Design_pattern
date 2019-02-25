/*
iterator pattern - 효율적으로 객체 컬렉션을 반복할 수 있게 해줌. next메소드를 사용해서 다음 순서의 요소를 반환
*/
class iterator {
    constructor(items){

        this.index = 0;
        this.items = items;
    }
    first(){
        this.reset();
        return this.next();
    }
    current(){
        return {
            done: false,
            value: this.items[this.index++]
        }
    }
    next(){
        const val = this.items[this.index++];
        if(this.hasNext()){
            return {
                done: false,
                val,
            };
        }
        return {done:true};
    }
    hasNext(){
        return this.index <= this.items.length;
    }
    reset(){
        this.index = 0;
    }
    each(callback){
        for (let item = this.first(); this.hasNext(); item = this.next()) {
            callback(item);
        }
    }
}
const items = ['one', 2, '삼', '4'];
const iterable = new iterator(items);
console.log(iterator.prototype.da);
while (iterable.hasNext()) {
    console.log(iterable.next());
    // { done: false, value: 'one' }
    // { done: false, value: 2 }
    // { done: false, value: '삼' }
    // { done: false, value: '4' }
    // { done: true }
}

iterable.first(); // { done: false, value: 'one' }

iterable.each(console.log);
// { done: false, value: 'one' }
// { done: false, value: 2 }
// { done: false, value: '삼' }
// { done: false, value: '4' }