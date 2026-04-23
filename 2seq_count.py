{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b2bdfd5-a877-42d8-a6d1-bd7459b6c11a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'AAATCGGGTTTCTCTAGAGCCC' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m dna = \u001b[43mAAATCGGGTTTCTCTAGAGCCC\u001b[49m\n\u001b[32m      2\u001b[39m Total_length = \u001b[38;5;28mlen\u001b[39m(dna)\n",
      "\u001b[31mNameError\u001b[39m: name 'AAATCGGGTTTCTCTAGAGCCC' is not defined"
     ]
    }
   ],
   "source": [
    "dna = AAATCGGGTTTCTCTAGAGCCC\n",
    "Total_length = len(dna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "afbe11cb-9427-46c4-abc2-0509d80f3617",
   "metadata": {},
   "outputs": [],
   "source": [
    "dna = \"AAATCGGGTTTCTCTAGAGCCC\"\n",
    "Total_length = len(dna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9812b38b-add7-4c3c-aa64-f052c42338ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "dna = \"AAATCGGGTTTCTCTAGAGCCC\"\n",
    "Total_length = len(dna)\n",
    "print (Total_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "daab01f0-e9ce-4078-a4e9-fa784ad52c90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "0.5\n"
     ]
    }
   ],
   "source": [
    "dna = \"AAATCGGGTTTCTCTAGAGCCC\"\n",
    "Total_length = len(dna)\n",
    "print (Total_length)\n",
    "A = dna.count(\"A\")\n",
    "T = dna.count(\"T\")\n",
    "G = dna.count(\"G\")\n",
    "C = dna.count(\"C\")\n",
    "GC_count = (G+C) / len(dna)\n",
    "print (GC_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "70b00bff-fa38-40a6-a8c5-16a18e11bd8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "50.0\n"
     ]
    }
   ],
   "source": [
    "dna = \"AAATCGGGTTTCTCTAGAGCCC\"\n",
    "Total_length = len(dna)\n",
    "print (Total_length)\n",
    "A = dna.count(\"A\")\n",
    "T = dna.count(\"T\")\n",
    "G = dna.count(\"G\")\n",
    "C = dna.count(\"C\")\n",
    "GC_count = (G+C) / len(dna) * 100\n",
    "print (GC_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b6813a85-f6b2-4523-91cb-1d2367fffde3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "50.0\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "dna = \"AAATCGGGTTTCTCTAGAGCCC\"\n",
    "Total_length = len(dna)\n",
    "print (Total_length)\n",
    "A = dna.count(\"A\")\n",
    "T = dna.count(\"T\")\n",
    "G = dna.count(\"G\")\n",
    "C = dna.count(\"C\")\n",
    "GC_count = (G+C) / len(dna) * 100\n",
    "print (GC_count)\n",
    "passed_quality = GC_count >= 50\n",
    "print (passed_quality)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "77e91695-d09d-450a-8bbb-11f68cb722c9",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'sample_fasta'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# Read FASTA file\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m file = \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43msample_fasta\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m      4\u001b[39m sequences = {}\n\u001b[32m      5\u001b[39m current_seq = \u001b[33m\"\u001b[39m\u001b[33m\"\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'sample_fasta'"
     ]
    }
   ],
   "source": [
    "# Read FASTA file\n",
    "file = open(\"sample_fasta\", \"r\")\n",
    "\n",
    "sequences = {}\n",
    "current_seq = \"\"\n",
    "\n",
    "for line in file:\n",
    "    line = line.strip()\n",
    "    \n",
    "    if line.startswith(\">\"):\n",
    "        current_seq = line\n",
    "        sequences[current_seq] = \"\"\n",
    "    else:\n",
    "        sequences[current_seq] += line\n",
    "\n",
    "file.close()\n",
    "\n",
    "# Print sequences\n",
    "print(sequences)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ec74e792-2ddb-448e-a303-61ca254af36e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'U70615.1 HIV-1 patient 4, clone 1, envelope glycoprotein (env) gene, V3 loop, partial cds': 'TGTACAAGGCCCAACAATAATATAAGACAAAGGATACATACAGGACCAGGGCAAGGGCAAGCACTCTATACAACAAGGATAACAGGAGACATAAGAAAAGCATATTGT'}\n",
      "49\n",
      "20\n",
      "23\n",
      "16\n",
      ">U70615.1 HIV-1 patient 4, clone 1, envelope glycoprotein (env) gene, V3 loop, partial cds GC content: 39.81481481481482\n",
      "False\n",
      "AT content: 60.18518518518518\n",
      "108\n"
     ]
    }
   ],
   "source": [
    "# Read FASTA file\n",
    "file = open(\"sample_fasta.txt\", \"r\")\n",
    "\n",
    "sequences = {}\n",
    "current_seq = \"\"\n",
    "\n",
    "for line in file:\n",
    "    line = line.strip()\n",
    "    \n",
    "    if line.startswith(\">\"):\n",
    "        current_seq = line[1:]\n",
    "        sequences[current_seq] = \"\"\n",
    "    else:\n",
    "        sequences[current_seq] += line\n",
    "\n",
    "file.close()\n",
    "\n",
    "# Print sequences\n",
    "print(sequences)\n",
    "\n",
    "G = seq.count(\"G\")\n",
    "C = seq.count(\"C\")\n",
    "A = seq.count(\"A\")\n",
    "T = seq.count(\"T\")    \n",
    "print (A)\n",
    "print (C)\n",
    "print (G)\n",
    "print (T)\n",
    "\n",
    "gc_content = (G + C) / len(seq) * 100\n",
    "    \n",
    "print(name, \"GC content:\", gc_content)\n",
    "\n",
    "QC_pass = gc_content >50\n",
    "print (QC_pass)\n",
    "\n",
    "type (QC_pass)\n",
    "at_content = (A + T) / len(seq) * 100\n",
    "    \n",
    "print(\"AT content:\", at_content)\n",
    "total_length = len(seq)\n",
    "print (total_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ccf550f7-a023-43e0-b02b-167638ce181a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'U70615.1 HIV-1 patient 4, clone 1, envelope glycoprotein (env) gene, V3 loop, partial cds': 'TGTACAAGGCCCAACAATAATATAAGACAAAGGATACATACAGGACCAGGGCAAGGGCAAGCACTCTATACAACAAGGATAACAGGAGACATAAGAAAAGCATATTGT'}\n",
      "Sequence: U70615.1 HIV-1 patient 4, clone 1, envelope glycoprotein (env) gene, V3 loop, partial cds\n",
      "A: 49\n",
      "C: 20\n",
      "G: 23\n",
      "T: 16\n",
      "GC content: 39.81481481481482\n",
      "QC pass (>50% GC): False\n",
      "AT content: 60.18518518518518\n",
      "Length: 108\n",
      "----------------------------------------\n"
     ]
    }
   ],
   "source": [
    "# Read FASTA file\n",
    "file = open(\"sample_fasta.txt\", \"r\")\n",
    "\n",
    "sequences = {}\n",
    "current_seq = \"\"\n",
    "\n",
    "for line in file:\n",
    "    line = line.strip()\n",
    "    \n",
    "    if line.startswith(\">\"):\n",
    "        current_seq = line[1:]\n",
    "        sequences[current_seq] = \"\"\n",
    "    else:\n",
    "        sequences[current_seq] += line\n",
    "\n",
    "file.close()\n",
    "\n",
    "# Print sequences\n",
    "print(sequences)\n",
    "\n",
    "# تحليل each sequence properly\n",
    "for name, seq in sequences.items():\n",
    "    \n",
    "    G = seq.count(\"G\")\n",
    "    C = seq.count(\"C\")\n",
    "    A = seq.count(\"A\")\n",
    "    T = seq.count(\"T\")    \n",
    "\n",
    "    print(\"Sequence:\", name)\n",
    "    print(\"A:\", A)\n",
    "    print(\"C:\", C)\n",
    "    print(\"G:\", G)\n",
    "    print(\"T:\", T)\n",
    "\n",
    "    gc_content = (G + C) / len(seq) * 100\n",
    "    print(\"GC content:\", gc_content)\n",
    "\n",
    "    QC_pass = gc_content > 50\n",
    "    print(\"QC pass (>50% GC):\", QC_pass)\n",
    "\n",
    "    at_content = (A + T) / len(seq) * 100\n",
    "    print(\"AT content:\", at_content)\n",
    "\n",
    "    total_length = len(seq)\n",
    "    print(\"Length:\", total_length)\n",
    "\n",
    "    print(\"-\" * 40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2431fb87-4cc4-443f-97bc-8ee6da1d44cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'U70615.1 HIV-1 patient 4, clone 1, envelope glycoprotein (env) gene, V3 loop, partial cds': 'TGTACAAGGCCCAACAATAATATAAGACAAAGGATACATACAGGACCAGGGCAAGGGCAAGCACTCTATACAACAAGGATAACAGGAGACATAAGAAAAGCATATTGT', 'PE027349.1 KR 1020220124646-A/27: COMPOSITION FOR DETECTION OF NEUTRALIZING ANTIBODY AGAINST SARS-COV2 VARIANTS, DECTECTION METHOD AND KIT COMPRISING THEREOF': 'ACCGAGTCTATCGTGCGGTTCCCCAACATCACCAACCTGTGTCCTTTCGACGAGGTGTTCAACGCCACCAGATTCGCCTCTGTGTACGCCTGGAACCGGAAGCGGATCTCTAACTGCGTGGCCGACTACTCCGTGCTGTACAACCTGGCCCCTTTCTTCACCTTCAAGTGCTACGGCGTGTCCCCTACCAAGCTGAACGACCTGTGCTTCACCAACGTGTACGCCGACTCCTTCGTGATCAGAGGCGACGAAGTGCGGCAGATCGCTCCTGGACAGACCGGCAACATCGCCGACTACAACTACAAGCTGCCCGACGACTTCACCGGCTGTGTGATCGCTTGGAACTCCAACAAGCTGGACTCCAAAGTCTCCGGCAACTACAATTACCTGTACCGGCTGTTCCGGAAGTCCAACCTGAAGCCTTTCGAGCGGGACATCTCCACCGAGATCTACCAGGCTGGCAATAAACCTTGTAATGGCGTGGCTGGCTTCAACTGCTACTTCCCACTGAAGTCCTACTCCTTCCGGCCTACATACGGCGTGGGCCATCAGCCTTACAGAGTGGTGGTGCTGTCCTTCGAGCTGCTGCATGCTCCTGCTACCGTGTGCGGCCCTAAGAAATCTACCAAC'}\n",
      "Sequence: U70615.1 HIV-1 patient 4, clone 1, envelope glycoprotein (env) gene, V3 loop, partial cds\n",
      "A: 49\n",
      "C: 20\n",
      "G: 23\n",
      "T: 16\n",
      "GC content: 39.81481481481482\n",
      "QC pass (>50% GC): False\n",
      "AT content: 60.18518518518518\n",
      "Length: 108\n",
      "----------------------------------------\n",
      "Sequence: PE027349.1 KR 1020220124646-A/27: COMPOSITION FOR DETECTION OF NEUTRALIZING ANTIBODY AGAINST SARS-COV2 VARIANTS, DECTECTION METHOD AND KIT COMPRISING THEREOF\n",
      "A: 133\n",
      "C: 208\n",
      "G: 149\n",
      "T: 140\n",
      "GC content: 56.666666666666664\n",
      "QC pass (>50% GC): True\n",
      "AT content: 43.333333333333336\n",
      "Length: 630\n",
      "----------------------------------------\n"
     ]
    }
   ],
   "source": [
    "# Read FASTA file \n",
    "file = open(\"sample_2seq.txt\", \"r\") \n",
    "sequences = {} \n",
    "current_seq = \"\" \n",
    "for line in file: \n",
    "    line = line.strip() \n",
    "    if line.startswith(\">\"): \n",
    "        current_seq = line[1:] \n",
    "        sequences[current_seq] = \"\" \n",
    "    else: sequences[current_seq] += line \n",
    "file.close() \n",
    "# Print sequences \n",
    "print(sequences) \n",
    "# تحليل each sequence properly \n",
    "for name, seq in sequences.items(): \n",
    "    G = seq.count(\"G\") \n",
    "    C = seq.count(\"C\") \n",
    "    A = seq.count(\"A\") \n",
    "    T = seq.count(\"T\") \n",
    "    print(\"Sequence:\", name) \n",
    "    print(\"A:\", A) \n",
    "    print(\"C:\", C) \n",
    "    print(\"G:\", G) \n",
    "    print(\"T:\", T) \n",
    "    gc_content = (G + C) / len(seq) * 100 \n",
    "    print(\"GC content:\", gc_content) \n",
    "    QC_pass = gc_content > 50 \n",
    "    print(\"QC pass (>50% GC):\", QC_pass) \n",
    "    at_content = (A + T) / len(seq) * 100 \n",
    "    print(\"AT content:\", at_content) \n",
    "    total_length = len(seq) \n",
    "    print(\"Length:\", total_length) \n",
    "    print(\"-\" * 40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d665393f-34ad-49cc-9206-7cec007a66ae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36503d49-6221-4a36-b5e4-7b7839e7fb5f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
