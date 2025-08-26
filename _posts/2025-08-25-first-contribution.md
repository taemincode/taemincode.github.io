---
layout: post
title: "How I Got My First Contribution for an Open Source Project"
date: 2025-08-25
categories: Open-Source
---

### 📌 Introduction
In this blog post, I would like to take you through how I got my first contribution for an open source library, which in this case was the Hugging Face [🤗 Transformers](https://github.com/huggingface/transformers) library. Although my contribution was not fixing or writing code (it was just translation), I'm still quite proud that I've made a contribution to a very important ML library!

The link to my PR: [https://github.com/huggingface/transformers/pull/39808](https://github.com/huggingface/transformers/pull/39808)

### 🌱 How It Happened
One day, I was just randomly thinking that it would be very cool to contribute to a big open source library. And since my ML skills were not enough to fix issues or add new lines of code, I had to think of some other way (you might think why I was so eager to do something - I don't know either 😬), and what I came up with was to translate documents, since I could speak both English and Korean (at that time, I actually thought I was a genius). So, after doing some research on documents of open source libraries (related to ML since that was where I wanted to contribute), I found the 🤗 Transformers library, which seemed to be actively translating their docs into different languages (including [Korean](https://github.com/huggingface/transformers/issues/20179)).

### 🌐 Translation
Since it was my first time, I struggled a bit in understanding how the translation for the documents worked. And it was more confusing because all the files in the toctree (which is a file that shows all the documents that are translated) were labeled as `in translation` (I thought that it meant that all the files were being translated by other people). So, I decided to ask about it, and I was able to clarify it with the help of the technical writer of this library.  
![Discussion](/assets/images/posts/2025/first-contribution/discussion.png)  
Now I understood how it worked, and it was time for the actual translation. I picked a file that was labeled as `in translation` (which actually meant that it was not translated yet; the file I chose was `text-to-speech.md`), and started translating it manually. However, it was only after opening the PR with my translated document that I realized that there was a translation guide explicitly made for Korean translations, which mentioned that our job wasn't to manually translate one by one, but use LLMs such as ChatGPT or Claude to first translate it, and then review if it flows naturally. Obviously, my manually translated document was declined, and I had to start it again. The new file that I chose was `gpt2.md`, and I started translating this time 'with LLMs'. After completing the tranlation (it only took like 20 minutes), I wrote the PR based on the template that was given. And after several days, my PR got reviewed by a couple of people and got [merged](https://github.com/huggingface/transformers/pull/39808)!

### 🙌 The Feeling
Although I felt kind of depressed when I found out that all my manual translation work ended up being nothing, I felt very proud and happy when my PR got merged. I really want to thank all the people who supportively helped and reviewed my translation.

### 💡 Why It Mattered
Through this experience, I learned that open source was not only for coding, but also for documentation, translations, and all the other stuff. Although it was just a small contribution, I felt that I became part of a global ML community. I also found that people in the ML community are all kind and supportive, and they are always there to help you (so don't be scared!). I will think of this just as the beginning of my open source journey, and I hope that in the future, I will be able to make more contributions that will benefit the community 😊