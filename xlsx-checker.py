import pandas as pd

# -------- Load Candidate File --------
file_path = r"C:\Users\Parth garg\Documents\GitHub\codeninjas\samples\expected.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nSummary statistics:")
print(df.describe())

# -------- 1. Required Column Check --------
required_cols = ["SR.", "NAME", "GENDER", "AGE", "DATE ", "COUNTRY"]
missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    print(f"\n⚠️ Missing required columns: {missing_cols}")
else:
    print("\n✅ All required columns exist.")

# -------- 2. Missing Values Check --------
if df.isnull().values.any():
    print("\n⚠️ Dataset contains missing values:")
    print(df.isnull().sum())
else:
    print("\n✅ No missing values found.")

# -------- 3. Formula / Business Rule Checks --------
if "AGE" in df.columns:
    invalid_age = df[df["AGE"] < 18]
    if not invalid_age.empty:
        print("\n⚠️ Formula/Rule check failed: Found AGE < 18")
        print(invalid_age)
    else:
        print("\n✅ AGE column passes rule check (all >= 18).")

    total_age = df["AGE"].sum()
    avg_age = df["AGE"].mean()
    print(f"\nAverage AGE = {avg_age}")
    print(f"Total AGE = {total_age}")
else:
    print("\n⚠️ No 'AGE' column found.")

# -------- 3b. Gender Count --------
if "GENDER" in df.columns:
    gender_counts = df["GENDER"].value_counts()
    num_males = gender_counts.get("Male", 0)
    num_females = gender_counts.get("Female", 0)
    print(f"\nTotal Males: {num_males}")
    print(f"Total Females: {num_females}")
else:
    print("\n⚠️ No 'GENDER' column found.")

# -------- 3c. DATE Validity Check --------
if "DATE " in df.columns:
    try:
        pd.to_datetime(df["DATE "], errors="raise", dayfirst=True)
        print("\n✅ DATE column values are valid dates.")
    except Exception as e:
        print(f"\n⚠️ Invalid date values found: {e}")
else:
    print("\n⚠️ No 'DATE ' column found.")

# -------- 3d. Duplicate Row Check --------
duplicate_rows = df[df.duplicated(keep=False) & df.notnull().all(axis=1)]
if not duplicate_rows.empty:
    print("\n⚠️ Found fully duplicate rows (all columns match):")
    # Show Excel-style row numbers (+2 because pandas index starts at 0 and header row is row 1)
    print("Row numbers:", (duplicate_rows.index + 2).tolist())
    print(duplicate_rows)
else:
    print("\n✅ No fully duplicate rows found.")

# -------- 3e. Empty Row Check --------
empty_rows = df[df.isnull().all(axis=1)]
if not empty_rows.empty:
    print("\n⚠️ Found completely empty rows:")
    print("Row numbers:", (empty_rows.index + 2).tolist())
    print(empty_rows)
else:
    print("\n✅ No completely empty rows found.")

# -------- 4. Compare with Expected Answer Sheet --------
try:
    expected_file = r"C:\Users\Parth garg\Documents\GitHub\codeninjas\samples\Free_Test_Data_100KB_XLSX.xlsx"
    df_expected = pd.read_excel(expected_file, engine="openpyxl")

    # --- Structural Comparison ---
    print("\n--- STRUCTURAL COMPARISON ---")
    results = {}

    # Row count
    row_match = (len(df) == len(df_expected))
    results["row_count"] = 100.0 if row_match else (min(len(df), len(df_expected)) / max(len(df), len(df_expected))) * 100

    # Column count
    col_match = (len(df.columns) == len(df_expected.columns))
    results["col_count"] = 100.0 if col_match else (min(len(df.columns), len(df_expected.columns)) / max(len(df.columns), len(df_expected.columns))) * 100

    # Age statistics similarity
    if "AGE" in df.columns and "AGE" in df_expected.columns:
        age_stats = ["mean", "std", "min", "max"]
        diffs = []
        for stat in age_stats:
            try:
                val1 = getattr(df["AGE"], stat)()
                val2 = getattr(df_expected["AGE"], stat)()
                diffs.append(abs(val1 - val2) / max(val1, val2) if max(val1, val2) != 0 else 0)
            except Exception:
                diffs.append(1)
        results["age_stats"] = (1 - sum(diffs) / len(diffs)) * 100
    else:
        results["age_stats"] = 0

    # Gender distribution similarity
    if "GENDER" in df.columns and "GENDER" in df_expected.columns:
        candidate_counts = df["GENDER"].value_counts(normalize=True)
        expected_counts = df_expected["GENDER"].value_counts(normalize=True)
        male_diff = abs(candidate_counts.get("Male", 0) - expected_counts.get("Male", 0))
        female_diff = abs(candidate_counts.get("Female", 0) - expected_counts.get("Female", 0))
        results["gender_dist"] = (1 - (male_diff + female_diff) / 2) * 100
    else:
        results["gender_dist"] = 0

    # Final structural match score
    structural_score = sum(results.values()) / len(results)
    print(f"📊 Structural Match Score: {structural_score:.2f}%")
    for k, v in results.items():
        print(f" - {k}: {v:.2f}%")

    # Missing / Extra columns
    missing_in_candidate = set(df_expected.columns) - set(df.columns)
    extra_in_candidate = set(df.columns) - set(df_expected.columns)
    if missing_in_candidate:
        print(f"\n⚠️ Missing columns compared to expected: {missing_in_candidate}")
    if extra_in_candidate:
        print(f"⚠️ Extra columns in candidate sheet: {extra_in_candidate}")

except FileNotFoundError:
    print("\nℹ️ No expected answer sheet found. Skipping comparison.")
