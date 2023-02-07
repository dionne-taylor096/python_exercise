{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1e110902",
   "metadata": {},
   "source": [
    "# Question 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "32c175b4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(99.9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b5b0e1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(\"False\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61771bf5",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da45b6d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "type('0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c8df77c",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc9803bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "type([{}])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65cb7a30",
   "metadata": {},
   "outputs": [],
   "source": [
    "type({'a': []})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b31890e1",
   "metadata": {},
   "source": [
    "# Question 2\n",
    "\n",
    "2. What data type would best represent the following?\n",
    "\n",
    "- A term or phrase typed into a search box. String\n",
    "- Whether or not a user is logged in. Boolean\n",
    "- A discount amount to apply to a user's shopping cart. Float/int\n",
    "- Whether or not a coupon code is valid. String\n",
    "- An email address typed into a registration form. String\n",
    "- The price of a product. int/float\n",
    "- The email addresses collected from a registration form. String\n",
    "- Information about applicants to Codeup's data science program. Dictionary/String"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a71f2f1d",
   "metadata": {},
   "source": [
    "# Question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "b99cd639",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[63], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m1\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m2\u001b[39;49m\n",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "'1' + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8381010",
   "metadata": {},
   "outputs": [],
   "source": [
    "6 % 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01e72519",
   "metadata": {},
   "outputs": [],
   "source": [
    "type (6 % 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a915add6",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(type(6 % 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74e4a2a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "'3 + 4 is ' + 3 + 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d2d4ee0",
   "metadata": {},
   "outputs": [],
   "source": [
    "0 < 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb8373bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "'False' == False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c67014fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "True == 'True'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31104799",
   "metadata": {},
   "outputs": [],
   "source": [
    "5 >= -5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab288641",
   "metadata": {},
   "outputs": [],
   "source": [
    "True or \"42\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0b2fdff",
   "metadata": {},
   "outputs": [],
   "source": [
    "6 % 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f140fa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < 4 and 1 == 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e3fb88a",
   "metadata": {},
   "outputs": [],
   "source": [
    "'codeup' == 'codeup' and 'codeup' == 'Codeup'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a348c343",
   "metadata": {},
   "outputs": [],
   "source": [
    "4 >= 0 and 1 !== '1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09c5791a",
   "metadata": {},
   "outputs": [],
   "source": [
    "6 % 3 == 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd37f808",
   "metadata": {},
   "outputs": [],
   "source": [
    "5 % 2 != 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b79b1c8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08bcbe92",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] + [2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bf63124",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "ad141343",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can't multiply sequence by non-int of type 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[64], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43m[\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43m \u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m]\u001b[49m\n",
      "\u001b[0;31mTypeError\u001b[0m: can't multiply sequence by non-int of type 'list'"
     ]
    }
   ],
   "source": [
    "[1] * [2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5a0e731",
   "metadata": {},
   "outputs": [],
   "source": [
    "[] + [] == []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da07a5f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "{} + {}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75ac1f85",
   "metadata": {},
   "source": [
    "# Questions 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58004175",
   "metadata": {},
   "outputs": [],
   "source": [
    "the_little_mermaid = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "492716e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "brother_bear = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b4dc4f0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "hercules = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fb2851b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daily_rent_fee = float(3.00)\n",
    "daily_rent_fee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6c1942a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rental_cost = (daily_rent_fee * the_little_mermaid) + (daily_rent_fee * hercules) + (daily_rent_fee * brother_bear)\n",
    "rental_cost"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1be48647",
   "metadata": {},
   "source": [
    "# Questions 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bef29cff",
   "metadata": {},
   "outputs": [],
   "source": [
    "hourly_rate_google = float(400.00)\n",
    "hourly_rate_facebook = float(350.00)\n",
    "hourly_rate_amazon = float(380.00)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "53d90948",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2400.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daily_rate_google = hourly_rate_google * 6\n",
    "daily_rate_google"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0c49ebca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1520.0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daily_rate_amazon = hourly_rate_amazon * 4\n",
    "daily_rate_amazon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9f688dfc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3500.0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daily_rate_facebook = hourly_rate_facebook * 10\n",
    "daily_rate_facebook"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a92d19be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7420"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weekly_payment_amount = daily_rate_facebook + daily_rate_google + daily_rate_amazon\n",
    "round(weekly_payment_amount)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a0d856b",
   "metadata": {},
   "source": [
    "# Questions 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cd83f068",
   "metadata": {},
   "outputs": [],
   "source": [
    "class_not_full = False\n",
    "class_full = True\n",
    "class_schedule_no_conflicts = True\n",
    "class_schedule_conflict = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4d84f925",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "enrolled_student = class_not_full and class_schedule_conflict\n",
    "enrolled_student"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a074b26c",
   "metadata": {},
   "source": [
    "# Questions 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f357eeb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "more_than_two_items = True\n",
    "less_than_two_items = False\n",
    "offer_not_expired = True\n",
    "offer_expired = False\n",
    "premium_member = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1845a02f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_offer_applied = less_than_two_items and offer_not_expired or premium_member\n",
    "product_offer_applied"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7e913e51",
   "metadata": {},
   "outputs": [],
   "source": [
    "username = 'codeup'\n",
    "password = 'notastrongpassword'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1a3bd752",
   "metadata": {},
   "outputs": [],
   "source": [
    "len(password) > 5 and len(username) >= 20 == True\n",
    "password != username == True\n",
    "password_count = password.count(\" \") > 0 == False\n",
    "username_count = username.count(\" \") > 0 == False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "dd9543a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pass_user_check = len(password) > 5 and len(username) <= 20 and password != username \n",
    "pass_user_check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "534db713",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pass_user_char_check = password_count or username_count\n",
    "pass_user_char_check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdb40ba6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c8b929c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
