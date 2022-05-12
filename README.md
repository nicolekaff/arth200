# Art History Image Randomizer 
This project serves as an art history study platform for students. The web interface allows for flash-card memorization of single works and their tombstone information as well as for practice writing pairwise comparisons. Instructors may customize the works included on the webpage to fit the individual curriculum of their course, and the page may be updated regularly before exams or as works are covered in class. 

This platform was designed to be easy to set up and to maintain. No knowledge of Git/GitHub, JavaScript, or HTML/CSS is necessary. 

## Starting Fresh
### Setting up a GitHub Repository
1. Sign in to an existing GitHub account or [create a new account](https://github.com/signup). 
2. Click your user icon in the top right. Then select Your respositories -> New.
3. Ensure that the owner of the repository matches your Github username.
4. Give the respository a name. The name of the respository will become part of the URL of the final webpage. It should not contain any spaces (use hypens instead) or any special characters. 
5. Ensure that the visibility of the respository is set to Public.
6. The default options are fine for the remaining settings 
    - "Add a README file" is unchecked
    - .gitignore template is set to None
    - License is set to None
7. Click "Create repository".

### Populating the Repository 
1. Go to the [arth-pair-practice respository](https://github.com/nicolekaff/arth-pair-practice)
2. Click the green **Code** button at the top and select **Download ZIP**.
3. Unzip the downloaded file **arth-pair-practice-main.zip**.
4. Enter the unzipped **arth-pair-practice-main** folder and then open the file **code.js**. *Note: You can open **code.js** in any text editor, including Notepad on Windows (right click -> Open with -> Notepad) or TextEdit on Mac (right click -> Open with -> TextEdit)* 
6. Update lines 4-7 of **code.js** by replacing the text within quotations with your information (keep the quotations and the semicolon). The USER_NAME should match your Github account username, REPO_NAME should be the name of the Github respository that you created. COURSE should be the course code for which the webpage is intended for. See below for an example where the Github username is nicolekaff, the repository name is arth-pair-practice, and the course code is ARTH200. 
```javascript
// Constants - update these as needed!
const USER_NAME = "nicolekaff";
const REPO_NAME = "arth-pair-practice";
const COURSE = "ARTH200";
```
7. Save **code.js** and close the file. 
8. Enter the **data** folder and then copy and paste your initial images into the **imgs** sub-folder. The default images that come with the repository download can be deleted if desired. 
9. Enter the **meta** sub-folder. Copy and paste the initial metadata files into the corresponding **architecture** and **art** folders. Again, the default data files that come with the repository download can be deleted if desired. See the **Formatting the Data** section below for instructions on how the data should be formatted. 
10. Return to your newly created empty Github respository. With the **Code** tab selected, click **upload an existing file** at the top under **Quick setup**. 
11. Go to the innermost **arth-pair-practice-main** folder in your file explorer and select all of the files/subfolders. Click and drag these into the area labeled **Drag fies here to add them to your repository.** *Note: It is important that the click-and-drag method is used rather than clicking "choose your files* and uploading from there. Clicking and dragging ensures that the all files in the data subfolder will be properly uploaded.
12. At the bottom of the page click **Commit changes**. 

### Making the Webpage Live
1. Click the **Settings** tab of your repository.
2. Click **Pages** on the left sidebar under **Code and automation**.
3. Under **Source** it should say that GitHub pages is currently disabled. In the dropdown menu change the selected option from **None** to **main** and then hit **Save**. 
4. A message should appear telling you that your site is ready to be published. Clicking the link should take you to the live webpage. *Note: It may take a few minutes for the webpage to show up, as GitHub needs time to build, deploy, and check the page status. Refreshing the page should render it when it's ready.*

## Formatting the Data
Every work uploaded to the webpage needs both an image and a metadata file. 
#### Images
- All images will be placed in **data/imgs** regardless of whether they are categorized as art or architcture. 
- Images can be of type **PNG** or **JPEG/JPG**.
- It is best to give images meaningful names and to avoid spaces/special characters. Below are some examples of good file names:
   - *Temple of Portunus* -> **temple_of_portunus.jpg**
   - Sculpture of *Akhenaten* -> **akhenaten.jpg** or **sculpture_of_akhenaten.jpg**
#### Metadata
- Metadata will be placed in **data/meta/architecture** or **data/meta/art** depending on the work's categorization.
- Data files must be in JavaScript Object Notation (JSON) format with the following four (case-sensitive) fields:
    - **metadata** (tombstone information for the work)
    - **period**
    - **category**
    - **image** (must match the file name of the corresponding image)
- To create a JSON file, open a blank file in a text editor and save it with the **.json** extension.
- The JSON file name can be anything (it can, but does not need to match the image file name), although a meaningful naming system can be useful for resusing files later.
- Below is the contents of a JSON file for a sculpture of *Akhenaten*. 
```
{
    "metadata": "Akhenaten, from Karnak, Thebes, 1353-1335 BCE. Sandstone, Egytpian Museum, Cairo",
    "period": "Egyptian",
    "category": "Sculpture",
    "image": "akhenaten.jpg"
}
```

## Updating the Page
Use the following steps to add new images to the webpage:
1. On the GitHub repository, enter the **data** folder and then the **imgs** folder. 
2. In the upper right, select **Add file -> Upload files**.
3. Drag and drop the new images or select **choose your files** and upload them from there.
4. At the bottom, ensure that **Commit directly to the main branch** is selected and then click **Commit changes**. 

Use the following steps to add the corresponding data files for the new images:
1. On the GitHub repository, enter the **data** folder and then the **meta** folder. 
2. Enter the **architecture** folder.
3. In the upper right, select **Add file -> Upload files**.
4. Drag and drop the new data files for all architecture pieces or select **choose your files** and upload them from there.
5. At the bottom, ensure that **Commit directly to the main branch** is selected and then click **Commit changes**. 
6. Go back to the **meta** folder and then enter the **art** folder.
7. Repeat steps 3-5 for the artwork data pieces. 

## Credit
This repository was created by Nicole Kaff in the Michelle Smith Collaboratory for Visual Culture as a resource for the [ARTH Visual Analysis Practice](http://2020collabsandbox8.artinterp.org/omeka/home-page) project, in support of the ARTH200 course at the University of Maryland.<br>

**Concept:** Alicia Perkovich<br>
**Research:** Alicia Perkovich, Amanda K. Chen<br>
**Omeka site:** Amanda K. Chen<br>
**Image Randomizer site:** Nicole Kaff<br>
**General Advising:** Quint Gregory and Chris Cloke

