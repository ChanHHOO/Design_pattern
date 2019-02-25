/* decorator pattern - 상황에 따라 객체에 부가 기능을 추가하는 패턴 */

class espresso{
    constructor(){
        this.cost = 2500;
    }
}
class americano extends espresso{
    cost = 0;
    constructor(){
        super();
        const es = new espresso();
        this.cost = es.cost + 500;
        this.water = 500;
    }
}
class latte extends espresso{
    cost = 0;
    constructor(){
        super();
        const es = new espresso();
        this.cost = es.cost + 200;
        this.milk = 500;
    }
    
}



ame = new americano();
lat = new latte();