final int BTN_SIZE = 25;
final int MARGIN = 25;
final int NUM_WIDTH = 50;

String capitalize(String name) {
  // Turns "string" into "String"
  return name.substring(0, 1).toUpperCase() + name.substring(1);
}

/*
Before you get a headache from reading this:
-> class AttributeCustomizer {
     |
     L--> class SquareButton (abstract) {}
     |              ^
     L--> class MinusButton extends SquareButton {}
     |              ^
     L--> class PlusButton extends MinusButton {}
}
*/

class AttributeCustomizer
{
  String name;
  int y;
  
  int value = 10;
  
  MinusButton minus;
  PlusButton plus;
  
  public AttributeCustomizer(String name, int y){
    this.y = y;
    this.name = name;
    
    minus = new MinusButton(width - MARGIN - BTN_SIZE*2 - NUM_WIDTH);
    plus  = new PlusButton(width - MARGIN - BTN_SIZE);
  }
  
  void increment() {
    if (remainingPoints > 0) {
      remainingPoints --;
      this.value++;
    }
  }
  
  void decrement() {
    if (this.value > 0) {
      this.value --;
      remainingPoints ++;
    }
  }
  
  void click() {
    plus.click();
    minus.click();
  }
  
  void draw() {
    fill(0);
    textSize(24);
    textAlign(LEFT, TOP);
    text(capitalize(this.name) + ":", MARGIN, this.y);
    
    plus.draw();
    minus.draw();
    
    fill(0);
    textAlign(CENTER, TOP);
    text(this.value, width-MARGIN-50, this.y);
  }
  
  
  // Stuff that's similar to both buttons
  
  abstract class SquareButton
  {
    int x;
    
    SquareButton(int x){
      this.x = x;
    }
    
    boolean isMouseOver(){
      return x < mouseX && mouseX < x + BTN_SIZE
          && y < mouseY && mouseY < y + BTN_SIZE;
    }
    
    color getFillColor() {
      if (isMouseOver())
        if (mousePressed && mouseButton == LEFT)
          return 128;
        else
          return 192;
      else
        return 255;
    }
    
    void display() {
      fill(getFillColor());
      stroke(0);
      strokeWeight(5);
      rect(x, y, BTN_SIZE, BTN_SIZE);
    }
    
    void click() {
      if (isMouseOver() && mouseButton == LEFT) onClick();
    } // very DRY
    // such abstract
    abstract void onClick();

  }
  
  // Getting more specific...
  
  class MinusButton extends SquareButton
  {
    MinusButton(int x) {super(x);} // SAEM THING BLAH BLAH BLAH
    
    void draw() {
      super.display();
      line(x + 7, y + BTN_SIZE/2, x + BTN_SIZE - 7 , y + BTN_SIZE/2);
      // Yup, that's an horizonal bar.
    }
    
    void onClick() {
      decrement(); // MUHAHAHA Java inner classes FTW!
    }
    
  }
  
  // A "+" button is like a "-" one: 
  class PlusButton extends MinusButton // Clever clever inheritance
  {
    PlusButton(int x) {super(x);} // SAEM THING BLAH BLAH BLAH
    
    void draw() {
      super.draw(); // It only has a vertical bar besides the horizontal one!
      line(x + BTN_SIZE/2, y + 7, x + BTN_SIZE/2, y + BTN_SIZE - 7);
    }
    
    // (Oh, and it should increment that counter, not decrement like the other one)
    void onClick()
    {
      increment();
    }
    
  }
  
}











