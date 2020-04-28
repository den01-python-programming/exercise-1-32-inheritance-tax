# Exercise 1.32 - Inheritance Tax

People that receive gifts will be charged Inheritance Tax if they receive more than £325,000 in the 7 years before the donor's death.

If there’s Inheritance Tax to pay, it’s charged at 40% on gifts given in the 3 years before death.

Gifts made 3 to 7 years before your death are taxed on a sliding scale known as ‘taper relief’ - [https://www.gov.uk/inheritance-tax/gifts](https://www.gov.uk/inheritance-tax/gifts):

| Years between gift and death | Tax paid |
| -------------------- | ----------------------|
| less than 3      | 40%                   |
| 3 to 4     | 32%                |
| 4 to 5   | 24%                 |
| 5 to 6 | 16%                |
| 6 to 7   | 8%               |
| 7 to 8   | 0%               |

**Example:**
- Jenny died on 1 July 2018. She was not married or in a civil partnership when she died.
- Jenny left 3 gifts in the 7 years before her death:
- £300,000 to her brother 6.5 years before her death
- £50,000 to her sister 4.5 years before her death
- £150,000 to her friend 3.5 years before her death
- Jenny is not entitled to any other gift exemptions or reliefs.
- There’s a £325,000 inheritance tax threshold. Anything below this amount is tax free.
- £300,000 is used up by the gift Jenny gave her brother. There’s no tax to pay on his gift.
- The remaining £25,000 is used up by her £50,000 gift to her sister. There’s tax to pay on the amount not covered by the threshold. That means there’s tax to pay on £25,000 of the gift to Jenny’s sister at a rate of 24%.
- The £150,000 gift given to her friend is taxed at a rate of 32%.
- Jenny’s remaining estate was valued at £500,000 and charged at the usual 40% inheritance tax rate. Jenny used up the tax-free threshold on gifts given before her death.

Write a program that calculates the inheritance tax for a gift for a number of years after death.

This is how the program should work:

```plaintext
Inheritance:
*500000*
Years since death:
*3*
Tax: 56000
```


```plaintext
Inheritance:
*325000*
Years since death:
*2*
Tax: 0
```

```plaintext
Inheritance:
*625000*
Years since death:
*6*
Tax: 24000
```
