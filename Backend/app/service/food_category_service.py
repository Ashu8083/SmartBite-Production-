from fastapi import HTTPException
from app.repo.food_category_repo import FoodCategoryRepository
from app.schema.food_category_schema import FoodCategorySchema,UpadteFoodCategory

class FoodCategoryService:
    def __init__(self,food_category:FoodCategoryRepository):
        self.food_category=food_category
        
    def create_food_category_service(self,create_food_category:FoodCategorySchema):
        category=self.food_category.create_food_category_repo(create_food_category)
        return category
    
    def get_food_category_by_id(self,category_id:int):
        category=self.food_category.get_food_category_by_id(category_id)
        if category is None:
            raise HTTPException(
                status_code=404,
                detail="food category not found"
            )
        return category
    
    def get_food_category_by_name(self,name:str):
        category=self.food_category.get_food_category_by_name(name)
        if category is None:
            raise HTTPException(
                status_code=404,
                detail="food category not found with this name"
            )
        return category
    
    def get_all_food_category(self):
        category=self.food_category.get_all_food_category()
        if category is None:
            raise HTTPException(
                status_code=404,
                detail="food categories not found"
            )
        return category
    
    def update_food_category(self,category_id:int,food_category:UpadteFoodCategory):
        category=self.food_category.get_food_category_by_id(category_id)
        if category is None:
            raise HTTPException(
                status_code=404,
                detail="food category not found"
            )
        update=self.food_category.update_food_category(category,food_category)
        return update
    
    def delete_food_category(self,category_id:int):
        category=self.food_category.delete_food_category(category_id)
        if category is None:
            raise HTTPException(
                status_code=404,
                detail="food category not found"
            )
        delete=self.food_category.delete_food_category(category_id)
        return delete