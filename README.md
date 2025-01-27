# HTML-CSS-JS-Separator-and-Combiner

---

#### **English Guide**

---

### **Overview**
This Python script allows you to:
1. **Extract** CSS and JavaScript code from an HTML file and save them as separate files (`styles.css` and `scripts.js`).
2. **Combine** separate HTML, CSS, and JavaScript files into a single HTML file.

The script also includes a graphical user interface (GUI) built with `tkinter` for ease of use.

---

### **Requirements**
- Python 3.x installed on your system.
- Required Python libraries: `tkinter`, `os`, `re`, `shutil`.

---

### **How to Use**

#### **1. Running the Script**
- Save the script as `script.py`.
- Open a terminal or command prompt and navigate to the directory where the script is saved.
- Run the script using the following command:
  ```bash
  python script.py
  ```

#### **2. Using the GUI**
- **Input Files**:
  - For **Extract Mode**: Select an HTML file.
  - For **Combine Mode**: Select an HTML file, a CSS file, and a JavaScript file.
- **Output Directory**: Select the directory where the output files will be saved.
- **Mode Selection**:
  - Choose **Extract HTML/CSS/JS** to separate CSS and JavaScript from an HTML file.
  - Choose **Combine HTML/CSS/JS** to merge CSS and JavaScript into a single HTML file.
- Click **Process** to execute the selected operation.

#### **3. Output**
- **Extract Mode**:
  - Creates three files in the output directory:
    - `output.html`: The HTML file without embedded CSS and JavaScript.
    - `styles.css`: The extracted CSS code.
    - `scripts.js`: The extracted JavaScript code.
- **Combine Mode**:
  - Creates a single file named `combined.html` in the output directory, which includes the CSS and JavaScript code.

---


### **Creating an Executable (EXE)**
To convert the script into an executable file:
1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Run the following command:
   ```bash
   pyinstaller --onefile --windowed script.py
   ```
3. The executable will be created in the `dist` folder.

---

---

#### **راهنمای فارسی**

---

### **معرفی**
این اسکریپت پایتون به شما امکان می‌دهد:
1. **کدهای CSS و JavaScript** را از یک فایل HTML استخراج کرده و آن‌ها را در فایل‌های جداگانه (`styles.css` و `scripts.js`) ذخیره کنید.
2. **فایل‌های جداگانه HTML، CSS و JavaScript** را در یک فایل HTML ادغام کنید.

این اسکریپت شامل یک رابط کاربری گرافیکی (GUI) است که با استفاده از `tkinter` ساخته شده است.

---

### **نیازمندی‌ها**
- نصب شده بودن پایتون 3.x روی سیستم شما.
- کتابخانه‌های مورد نیاز پایتون: `tkinter`, `os`, `re`, `shutil`.

---

### **نحوه استفاده**

#### **1. اجرای اسکریپت**
- اسکریپت را با نام `script.py` ذخیره کنید.
- ترمینال یا خط فرمان را باز کرده و به دایرکتوری محل ذخیره‌سازی اسکریپت بروید.
- اسکریپت را با دستور زیر اجرا کنید:
  ```bash
  python script.py
  ```

#### **2. استفاده از رابط کاربری**
- **فایل‌های ورودی**:
  - برای **حالت استخراج**: یک فایل HTML انتخاب کنید.
  - برای **حالت ادغام**: یک فایل HTML، یک فایل CSS و یک فایل JavaScript انتخاب کنید.
- **دایرکتوری خروجی**: دایرکتوری مورد نظر برای ذخیره فایل‌های خروجی را انتخاب کنید.
- **انتخاب حالت**:
  - **استخراج HTML/CSS/JS** را انتخاب کنید تا کدهای CSS و JavaScript از فایل HTML جدا شوند.
  - **ادغام HTML/CSS/JS** را انتخاب کنید تا کدهای CSS و JavaScript در یک فایل HTML ادغام شوند.
- روی **Process** کلیک کنید تا عملیات مورد نظر انجام شود.

#### **3. خروجی**
- **حالت استخراج**:
  - سه فایل در دایرکتوری خروجی ایجاد می‌شود:
    - `output.html`: فایل HTML بدون کدهای CSS و JavaScript.
    - `styles.css`: کدهای CSS استخراج شده.
    - `scripts.js`: کدهای JavaScript استخراج شده.
- **حالت ادغام**:
  - یک فایل به نام `combined.html` در دایرکتوری خروجی ایجاد می‌شود که شامل کدهای CSS و JavaScript است.

---


### **ساخت فایل اجرایی (EXE)**
برای تبدیل اسکریپت به یک فایل اجرایی:
1. `PyInstaller` را نصب کنید:
   ```bash
   pip install pyinstaller
   ```
2. دستور زیر را اجرا کنید:
   ```bash
   pyinstaller --onefile --windowed script.py
   ```
3. فایل اجرایی در پوشه `dist` ایجاد می‌شود.

---
