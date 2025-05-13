# Python-Advane

## **Install Python and pip**
To install Python and pip, follow the steps below:

- For Linux (MacOS users can also follow similar steps):
    - `sudo apt install python3`
    - `sudo apt install python3-pip`
- Verify Python installation:
    - `python --version`
- Verify pip installation:
    - `pip --version`

---

## **Project Setup**

### **Blog-Project**

1. **Navigate to the project directory**:

    - `cd python-advance/blog_project`

2. **Create a virtual environment**:

    - `python3 -m venv "your-virtual-environment-name"`

3. **Activate the virtual environment**:

    - For MacOS/Linux:
        - `source your-virtual-environment/bin/activate`
    - For Windows:
        - `your-virtual-environment-name\Scripts\activate`

4. **Install dependencies**:

    - `pip freeze > requirements.txt`

5. **Set up database credentials and run the project**
    
    - `python manage.py runserver`

6. **Deactivate the virtual environment** when you're done:

    - `deactivate`

**Register Page**

![image](https://github.com/user-attachments/assets/3cd2bb62-bd1b-4922-80ff-365e26db845a)

**Login Page**

![image](https://github.com/user-attachments/assets/1fbe5589-d973-467a-9304-6a0b1d4b1dad)


**Create Blog**

![image](https://github.com/user-attachments/assets/95f56a46-ea28-4834-b0a2-c7543395fe64)

**Edit Blog**

![image](https://github.com/user-attachments/assets/4823a9f8-d818-45bc-a293-4b1d6c95429f)

**List Page**
![image](https://github.com/user-attachments/assets/3969c319-0db1-4de2-ba90-3a2ed2cb0da9)


### **Product-Catalog**

1. **Navigate to the project directory**:

    - `cd python-advance/product_catalog`

2. **Create a virtual environment**:

    - `python3 -m venv "your-virtual-environment-name"`

3. **Activate the virtual environment**:

    - For MacOS/Linux:
        - `source your-virtual-environment/bin/activate`
    - For Windows:
        - `your-virtual-environment-name\Scripts\activate`

4. **Install dependencies**:

    - `pip freeze > requirements.txt`

5. **Set up database credentials and run the project**
    
    - `python manage.py runserver`
      
6. **Run Test cases**
    
    - `python3 manage.py test catalog.tests`
      
    - ![image](https://github.com/user-attachments/assets/b963896b-d5a6-4b01-8136-461fce8796c2)


7. **Deactivate the virtual environment** when you're done:

    - `deactivate`

8. **Postman Document**
   - https://documenter.getpostman.com/view/39898232/2sB2jAcU4t
