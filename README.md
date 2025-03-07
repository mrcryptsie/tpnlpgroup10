# 🤖 IFRI Chatbot - Assistant Intelligent avec RAG 📚💡

Ce projet est un assistant basé sur **Chainlit** et **Hugging Face**, qui répond aux FAQ de l'Institut de Formation et de Recherche en Informatique (IFRI) - UAC.  
Il utilise un modèle **LLM (LLaMA 2)** combiné avec **un moteur de recherche RAG** pour extraire des réponses à partir de documents PDF.  

## ✨ Fonctionnalités
✅ **Recherche améliorée (RAG)** : Analyse des fichiers PDF pour des réponses précises.  
✅ **Modèle avancé (LLaMA 2 - 7B HF)** : Génération de texte intelligente.  
✅ **Mémoire conversationnelle** : Suivi du contexte pour des échanges fluides.  
✅ **Mode sombre et clair** : Logos adaptatifs.  
✅ **Déploiement facile** : Compatible avec **Hugging Face Spaces**.  

---

## 🚀 Installation et Exécution Locale  

### 🔹 **1. Cloner le projet**
```bash
git clone https://huggingface.co/spaces/ton-utilisateur/ton-projet
cd ton-projet
```

### 🔹 **2. Installer les dépendances**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Ajouter des fichiers PDF**
Place tes documents dans le dossier **`data/`**.

### 🔹 **4. Lancer l'application**
```bash
chainlit run app.py
```

L'interface sera accessible sur **`http://localhost:8000`** 🌍.  

---

## 🌍 Déploiement sur Hugging Face Spaces  
Tu peux **héberger gratuitement** ton assistant sur **Hugging Face Spaces** en suivant ces étapes :  

### **🔹 1. Créer un nouvel Espace**  
- Va sur **[Hugging Face Spaces](https://huggingface.co/spaces)**
- Clique sur **"Create New Space"**
- Choisis **"SDK: Python"**  

### **🔹 2. Ajouter les fichiers à l’espace**  
- **Téléverse ces fichiers** :  
  - `app.py`
  - `requirements.txt`
  - Dossier `public/` (**logos et favicon**)
  - Dossier `data/` (**fichiers PDF**)  

### **🔹 3. Déploiement Automatique**  
Une fois les fichiers ajoutés, Hugging Face Spaces **installera automatiquement** les dépendances et lancera l'application.  

✅ **Ton assistant est maintenant en ligne !** 🎉  

---

## 🏗️ **Structure du Projet**
```
mon_projet/
│── app.py               # Code principal du chatbot
│── requirements.txt      # Dépendances à installer
│── data/                 # 📂 Dossier contenant les fichiers PDF
│   ├── fichier1.pdf
│   ├── fichier2.pdf
│── public/               # 📂 Dossier pour les logos et favicon
│   ├── logo_light.png
│   ├── logo_dark.png
│   ├── favicon.png
│── README.md             # Documentation du projet
```

---

## 🔧 **Personnalisation**
🔹 **Changer le modèle LLM** :  
Modifie la ligne suivante dans `app.py` pour tester un autre modèle :
```python
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-2-7b-hf", task="text-generation")
```
Tu peux essayer **Mistral**, **Falcon**, ou **GPT-J**.  

🔹 **Modifier les logos et favicon** :  
Remplace `logo_light.png`, `logo_dark.png`, et `favicon.png` dans le dossier `public/`.  

---

## 🤝 Contribuer
Les contributions sont les bienvenues !  
Si tu veux **ajouter des fonctionnalités**, fais une **pull request** ou ouvre une **issue**.  

---




