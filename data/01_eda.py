{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a5b3d57",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "\n",
    "import pandas as pd\n",
    "\n",
    "# 读取数据\n",
    "df = pd.read_csv(\"data/WA_Fn-UseC_-Telco-Customer-Churn.csv\")\n",
    "\n",
    "# 基本检查\n",
    "print(df.shape)      # (7043, 21)\n",
    "df.head()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
