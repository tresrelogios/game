int remainingPoints = 20;
String[] attribute_names = {"size", "attack", "defense",
                            "intelligence", "luck", "stamina"};
                            
ArrayList<AttributeCustomizer> attributes;


void setup(){
  size(400, 600);
  
  attributes = new ArrayList<AttributeCustomizer>();
  int offset_y = 50;
  
  for (String name : attribute_names)
    attributes.add(new AttributeCustomizer(name, offset_y += 50));
}


void draw() {
  background(192);
  
  for (AttributeCustomizer attribute : attributes) {
    attribute.draw();
  }
  
  textSize(28);
  textAlign(CENTER, TOP);
  text("Costumize your character", width/2, 20);
  
  textSize(18);
  textAlign(RIGHT);
  text("Remaining points: " + remainingPoints, width-20, height-20);
}

void mouseReleased() {
  for (AttributeCustomizer attribute : attributes) {
    attribute.click();
  }
}
