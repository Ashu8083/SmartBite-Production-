from sqlalchemy.orm import Session
from app.model.food_category_model import FoodCategory
from app.schema.food_category_schema import FoodCategorySchema,UpadteFoodCategory

class FoodCategoryRepository:
    def __init__(self,db:Session):
        self.db=db
    
    def create_food_category_repo(self,food_category:FoodCategorySchema):
        category=FoodCategory(
            name=food_category.name,
            description=food_category.description
        )
        
        self.db.add(category)
        self.db.flush()
        return category
    
    def get_food_category_by_id(self,category_id:int):
        category=self.db.query(FoodCategory).filter(FoodCategory.id==category_id).first()
        return category
    
    def get_food_category_by_name(self,name:str):
        category=self.db.query(FoodCategory).filter(FoodCategory.name==name).first()
        return category
    
    def get_all_food_category(self):
        category=self.db.query(FoodCategory).all()
        return category
    
    def update_food_category(self,category:FoodCategory ,food_category:UpadteFoodCategory):


        for field ,value in food_category.model_dump(exclude_unset= True).items():
            setattr(category,field,value)

        self.db.add(category)
        self.db.flush()
        self.db.refresh(category)
        return category

        # if exisiting is None:
        #     return None
        # if food_category.name is not None:
        #     exisiting.name = food_category.name
        # if food_category.description is not None:
        #     exisiting.description = food_category.description
        # return exisiting
    
    def delete_food_category(self,delete_food_category : FoodCategory):

        self.db.delete(delete_food_category)
        self.db.flush()
        self.db.refresh(delete_food_category)
        
        return delete_food_category