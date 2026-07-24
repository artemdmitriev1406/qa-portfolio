# Selected Bug Reports — Mesto

## MESTO-01 — Updated profile data is not saved

**Priority:** Blocker  
**Status:** Open in the tested build

**Precondition:** The main page is open.

**Steps**

1. Open the profile editing modal.
2. Enter valid new values in the Name and Occupation fields.
3. Click **Save**.

**Expected result**

The modal closes and the new profile data is displayed on the main page.

**Actual result**

The previously stored values remain displayed; the entered data is not persisted.

**Impact**

A core profile-management flow is unavailable.

---

## MESTO-02 — Current occupation is missing in the edit form

**Priority:** High

**Steps**

1. Open the main page.
2. Open the profile editing modal.

**Expected result**

The Occupation field contains the current profile value.

**Actual result**

The field is empty.

**Impact**

The user cannot safely edit one field without re-entering the other value.

---

## MESTO-03 — Save remains enabled when Name is empty

**Priority:** High

**Precondition:** The profile editing modal is open.

**Steps**

1. Clear the Name field.
2. Enter a valid value in Occupation.

**Expected result**

The Save button is disabled and the required-field error is shown.

**Actual result**

The Save button remains enabled.

**Impact**

Invalid profile data can be submitted.

---

## MESTO-04 — Maximum-length validation is not shown

**Priority:** High

**Steps**

1. Open the profile editing modal.
2. Enter a value longer than the supported maximum in Name or Occupation.

**Expected result**

The field is marked invalid and an explanatory validation message is displayed.

**Actual result**

No validation message is displayed.

**Impact**

The interface does not explain why input is invalid and may allow inconsistent submission behaviour.

## Documentation notes

The original reports included exact browser version and training URL. Those values were removed from the public portfolio because the environment is temporary and not relevant to current reproduction.