questions = {
    "Beginner": [
        {
            "question": "What is the difference between a cell reference like A1 and $A$1?",
            "answer": "A1 is a relative reference, while $A$1 is an absolute reference.",
            "alternatives": ["relative vs absolute", "locked cell", "fixed reference"]
        },
        {
            "question": "How would you use the SUM function to add values in cells B2:B10?",
            "answer": "Use =SUM(B2:B10).",
            "alternatives": ["sum formula", "add range", "sum function"]
        },
        {
            "question": "What shortcut would you use to quickly copy a formula from one cell to another?",
            "answer": "Drag the fill handle or use Ctrl+C and Ctrl+V.",
            "alternatives": ["autofill", "copy formula", "ctrl+c ctrl+v", "drag corner"]
        },
        {
            "question": "How do you freeze the top row so that headers are always visible while scrolling?",
            "answer": "Use Freeze Panes → Freeze Top Row in the View tab.",
            "alternatives": ["freeze panes", "lock top row", "keep header visible"]
        },
        {
            "question": "How do you apply basic filters to a column in Excel?",
            "answer": "Select the column and click Filter in the Data tab.",
            "alternatives": ["apply filter", "data filter", "drop-down filter"]
        },
        {
            "question": "How do you insert a new row or column in Excel?",
            "answer": "Right-click the row/column header and select Insert.",
            "alternatives": ["insert row", "insert column", "add row column"]
        },
        {
            "question": "What is the difference between Save and Save As?",
            "answer": "Save updates the current file, Save As creates a new file with a new name or location.",
            "alternatives": ["save overwrite", "new copy", "different name save"]
        },
        {
            "question": "How can you quickly autofill a series of numbers or dates in Excel?",
            "answer": "Use the fill handle to drag across cells.",
            "alternatives": ["autofill", "drag fill", "series fill"]
        },
        {
            "question": "What is the purpose of the AVERAGE function?",
            "answer": "It calculates the mean of a set of values.",
            "alternatives": ["average values", "mean function", "calculate mean"]
        },
        {
            "question": "How do you merge cells and center the text?",
            "answer": "Select cells, click Merge & Center in the Home tab.",
            "alternatives": ["merge center", "combine cells", "center merge"]
        },
        {
            "question": "What is the shortcut to copy and paste in Excel?",
            "answer": "Ctrl+C to copy and Ctrl+V to paste.",
            "alternatives": ["copy paste", "ctrl+c ctrl+v", "shortcut copy paste"]
        },
        {
            "question": "How do you rename a worksheet?",
            "answer": "Right-click the sheet tab and choose Rename.",
            "alternatives": ["rename sheet", "change sheet name", "sheet rename"]
        },
        {
            "question": "How can you sort a column from A–Z or Z–A?",
            "answer": "Select the column and use Sort Ascending or Sort Descending in the Data tab.",
            "alternatives": ["sort ascending", "sort descending", "alphabetical sort"]
        },
        {
            "question": "What does the COUNT function do?",
            "answer": "It counts the number of numeric values in a range.",
            "alternatives": ["count numbers", "count numeric cells", "number count"]
        }
    ],
    "Intermediate": [
        {
            "question": "How would you use the VLOOKUP function? Can you explain its syntax?",
            "answer": "Use =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup]).",
            "alternatives": ["vlookup syntax", "vertical lookup", "lookup value in table"]
        },
        {
            "question": "When should you use IF function in Excel? Give an example.",
            "answer": "To return different values based on a condition. Example: =IF(A1>50,'Pass','Fail').",
            "alternatives": ["if logic", "conditional formula", "pass fail example"]
        },
        {
            "question": "How would you create a pivot table to summarize sales by region?",
            "answer": "Insert → PivotTable, drag Region to Rows and Sales to Values.",
            "alternatives": ["pivot table", "summarize sales", "group by region"]
        },
        {
            "question": "Explain the difference between COUNT, COUNTA, and COUNTIF.",
            "answer": "COUNT counts numbers, COUNTA counts non-empty cells, COUNTIF counts based on condition.",
            "alternatives": ["count numbers", "count non-empty", "count condition"]
        },
        {
            "question": "What’s the purpose of conditional formatting? Can you give an example?",
            "answer": "To automatically format cells based on rules (e.g., highlight values > 100).",
            "alternatives": ["highlight cells", "conditional rules", "formatting rule"]
        },
        {
            "question": "How would you combine text from two columns (e.g., First Name and Last Name) using a formula?",
            "answer": "Use =A1&\" \"&B1 or =CONCAT(A1, \" \", B1).",
            "alternatives": ["concatenate", "combine text", "merge columns"]
        },
        {
            "question": "Explain the difference between relative, absolute, and mixed cell references.",
            "answer": "Relative changes with copy, absolute stays fixed, mixed fixes row or column only.",
            "alternatives": ["cell references", "relative vs absolute", "mixed reference"]
        },
        {
            "question": "How do you use Data Validation to allow only numbers between 1 and 100 in a cell?",
            "answer": "Data → Data Validation → Whole number → between 1 and 100.",
            "alternatives": ["data validation", "restrict numbers", "allow range"]
        },
        {
            "question": "What does the TRIM function do, and when would you use it?",
            "answer": "TRIM removes extra spaces from text, leaving only single spaces.",
            "alternatives": ["remove spaces", "trim spaces", "clean text"]
        },
        {
            "question": "How do you create a drop-down list in Excel?",
            "answer": "Data → Data Validation → List and enter items.",
            "alternatives": ["dropdown", "data validation list", "drop down menu"]
        },
        {
            "question": "How do you use the IF function to assign 'Pass' if score ≥ 50, otherwise 'Fail'?",
            "answer": "Use =IF(A1>=50,'Pass','Fail').",
            "alternatives": ["if pass fail", "conditional pass fail", "if formula"]
        },
        {
            "question": "How do you find duplicate values in a column?",
            "answer": "Use Conditional Formatting → Highlight Duplicates or COUNTIF formula.",
            "alternatives": ["find duplicates", "highlight duplicates", "duplicate values"]
        },
        {
            "question": "What does the LEN function do, and give a use case.",
            "answer": "LEN returns the number of characters in a text string.",
            "alternatives": ["length of text", "count characters", "len function"]
        },
        {
            "question": "How do you protect a worksheet so others cannot edit it?",
            "answer": "Use Review → Protect Sheet and set a password.",
            "alternatives": ["protect sheet", "lock worksheet", "password protect"]
        }
    ],
    "Advanced": [
        {
            "question": "How would you use INDEX + MATCH as an alternative to VLOOKUP?",
            "answer": "Use =INDEX(return_range, MATCH(lookup_value, lookup_range, 0)).",
            "alternatives": ["index match", "alternative to vlookup", "flexible lookup"]
        },
        {
            "question": "What is Power Query in Excel, and how is it useful for data cleaning?",
            "answer": "Power Query is a tool to import, clean, and transform data.",
            "alternatives": ["data cleaning tool", "query editor", "transform data"]
        },
        {
            "question": "How would you create a dynamic chart that updates automatically when new data is added?",
            "answer": "Use a table as a data source or define a dynamic named range.",
            "alternatives": ["auto updating chart", "dynamic chart", "update with new data"]
        },
        {
            "question": "Explain how to write a nested IF formula to handle multiple conditions.",
            "answer": "Example: =IF(A1>80,'A',IF(A1>60,'B','C')).",
            "alternatives": ["nested ifs", "multiple conditions", "multi if formula"]
        },
        {
            "question": "What are macros in Excel? Can you describe a situation where you’d use them?",
            "answer": "A macro is a recorded set of actions to automate tasks, e.g., formatting reports.",
            "alternatives": ["vba macro", "automate tasks", "recorded actions"]
        },
        {
            "question": "How would you use the TEXT function to format a date?",
            "answer": "Use =TEXT(A1, \"dd-mm-yyyy\") to format as day-month-year.",
            "alternatives": ["text function", "format date", "date formatting"]
        },
        {
            "question": "How do you use array formulas or dynamic arrays like FILTER or UNIQUE in Excel 365?",
            "answer": "Use =FILTER(range, condition) or =UNIQUE(range).",
            "alternatives": ["array formula", "dynamic array", "filter unique"]
        },
        {
            "question": "Can you explain how to use the XLOOKUP function and how it improves on VLOOKUP?",
            "answer": "XLOOKUP replaces VLOOKUP, works both directions, and avoids column index issues.",
            "alternatives": ["xlookup", "better than vlookup", "lookup function"]
        },
        {
            "question": "How would you automate a monthly report using Pivot Tables and slicers?",
            "answer": "Create PivotTable, add slicers, refresh monthly data.",
            "alternatives": ["automate report", "pivot slicers", "monthly pivot"]
        },
        {
            "question": "What is the difference between Power Pivot and Power Query?",
            "answer": "Power Query is for data transformation, Power Pivot is for modeling and analysis.",
            "alternatives": ["power pivot vs query", "data model vs transform", "difference power tools"]
        },
        {
            "question": "How can you use the INDEX-MATCH combination, and why might it be better than VLOOKUP?",
            "answer": "INDEX-MATCH is more flexible and avoids issues with column order.",
            "alternatives": ["index match", "better than vlookup", "flexible lookup"]
        },
        {
            "question": "Explain how to use the OFFSET function in a formula.",
            "answer": "OFFSET returns a range offset from a starting point, e.g., =OFFSET(A1,1,1).",
            "alternatives": ["offset formula", "dynamic range", "offset function"]
        },
        {
            "question": "How would you use Power Query to clean and transform raw data?",
            "answer": "Import data into Power Query, apply steps like remove columns, split, filter.",
            "alternatives": ["power query clean", "transform raw data", "query editor"]
        },
        {
            "question": "How do you create a macro to automate a repetitive Excel task?",
            "answer": "Use View → Record Macro, perform actions, save, and run later.",
            "alternatives": ["record macro", "automate task", "macro record"]
        }
    ]
}

scenario_prompts = {
    "Beginner": """🟢 Beginner Task:
1. Create table with 5 students & marks in Math, Science, English
2. Add Total & Average columns
3. Use conditional formatting for marks < 40""",
    
    "Intermediate": """🟡 Intermediate Task:
1. Create 10 transactions with Date, Product, Category, Quantity, Unit Price
2. Add Total Sales (=Qty×Price)
3. Use Data Validation for Category
4. Use VLOOKUP/XLOOKUP from Price List
5. Create Pivot Table (Total Sales by Category)""",
    
    "Advanced": """🔴 Advanced Task:
1. Create dataset with 20+ rows (Date, Region, Salesperson, Product, Units, Sales Amount)
2. Add IF formula to classify High/Medium/Low
3. Create Pivot Table (Sales by Region & Salesperson)
4. Add Pivot Chart
5. (Bonus) Record Macro to refresh Pivot"""
}
