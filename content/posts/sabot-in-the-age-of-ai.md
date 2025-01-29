---
date: 2025-01-28
linktitle: sabot-in-the-age-of-ai
menu:
  main:
    parent: tutorials
title: "Sabot in the Age of AI"
weight: 10
---

<div class="caption"><img src="poison.madhouse-project.png">A captured screenshot showcasing the <code>iocaine</code> <a href="https://poison.madhouse-project.org/">demonstration</a> site in operation. The primary objective of <code>iocaine</code> is to generate a stable, infinite maze of randomized garbage. Each page is randomly generated but adheres to a consistent structure: an optional <em>'back'</em> link (pointing to <code>../</code>), followed by a series of Markov chain-generated paragraphs of varying lengths, and an unordered list of links at the bottom. Each link is relative to the current page and features a randomized URI along with accompanying randomized text. Additional details on its functionality can be found on the <a href="https://iocaine.madhouse-project.org/">dedicated website</a>.</div>

{{% hint danger %}}
### Warning

Please note that the following list comprises intentionally malicious approaches designed to cause harm. Do not deploy any of these suggestions unless you are fully cognizant of the potential consequences of your actions. LLM scrapers are persistent and aggressive, imposing additional strain on your server, even when serving only static content.
{{% /hint %}}

## Context

This formulated list diligently records strategically offensive methodologies and purposefully orchestrated tactics intended to facilitate (algorithmic) sabotage, including the deliberate disruption of systems and processes, alongside the targeted poisoning or corruption of data within the operational workflows of artificial intelligence (AI) systems. These approaches seek to destabilize critical mechanisms, undermine foundational structures, and challenge the overall reliability, functionality, and integrity of AI-driven frameworks.

###  List of Resources

**Table 1: Offensive Methods and Strategic Approaches for Facilitating (Algorithmic) Sabotage, Framework Disruption, and Intentional Data Poisoning**

| **No.** | **Tool/Method**         | **Description**                                                                                                                                                                                                                                                                                         | **Source**                                             |
|---------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| 1.      | **`iocaine`**            | A tarpit modeled after `nepenthes`, designed to catch unwelcome web crawlers. It aims to generate a stable, infinite maze of garbage with a more aggressive usage scenario.                                                                         | [URL](https://git.madhouse-project.org/algernon/iocaine) |
| 2.      | **`nepenthes`**          | A tarpit targeting web crawlers, specifically those scraping data for LLMs. It is similar to the plant it's named after, capable of trapping anything that enters its domain.                                                                | [URL](https://zadzmo.org/code/nepenthes/)               |
| 3.      | **`quixotic`**           | A program designed to feed fake content to bots and `robots.txt`-ignoring LLM scrapers using a simple Markov Chain text generator.                                                                                                               | [URL](https://marcusb.org/hacks/quixotic.html)          |
| 4.      | **`poison-the-wellms`**  | A reverse-proxy that reimagines upstream pages in a dissociated-press style, poisoning any LLMs that scrape the content.                                                                                                                       | [URL](https://codeberg.org/MikeCoats/poison-the-wellms) |
| 5.      | **`django-llm-poison`**  | A pluggable [Django](https://www.djangoproject.com/) application that replaces a subset of text content with nonsense when served to AI crawlers. Inspired by `quixotic`.                                                                 | [URL](https://github.com/Fingel/django-llm-poison)     |
| 6.      | **`konterfai`**          | A proof-of-concept model-poisoner for LLMs that generates nonsensical content ("bullshit") to degrade these models.                                                                                                                           | [URL](https://codeberg.org/konterfai/konterfai)        |
| 7.      | **`caddy-defender`**     | A middleware plugin for [Caddy](https://caddyserver.com/) that blocks or manipulates requests based on client IP. Useful for preventing unwanted traffic or polluting AI training data with garbage responses.                                | [URL](https://github.com/JasonLovesDoggo/caddy-defender)|
| 8.      | **`marko`**              | Implements the [Dissociated Press](https://en.wikipedia.org/wiki/Dissociated_press) algorithm as both a library and CLI tool. It generates indefinite output based on character- or word-based Markov models.                                  | [URL](https://codeberg.org/timmc/marko/)               |
| 9.      | **`markov-tarpit`**              | This software can run as a back-end for a webserver, in order to trickle out a Markov chain generated output. The intended use is tarpitting "AI" bots while feeding them, slowly, useless data.                                  | [URL](https://git.rys.io/libre/markov-tarpit)               |
| 10.      | **`spigot`**              | A hierarchy of Markov Chain generated web pages. This is a simple proof of concept of using a Markov Chain to generate an infinitely large website.                                 | [URL](https://github.com/gw1urf/spigot)               |

<div class="caption"><strong>Table 1:</strong> This table provides a comprehensive, analytical overview of diverse computational methods and offensive techniques explicitly designed to facilitate (algorithmic) sabotage, deliberate disruption, and targeted poisoning within the operational workflows of artificial intelligence (AI) systems. Each resource delineated herein has been meticulously structured to erode the integrity of AI models, with particular emphasis on destabilizing their data acquisition mechanisms, subverting training pipelines, and circumventing the foundational operational frameworks that underpin their functionality and reliability.</div>

<span style="color:grey">* Please note that this list was last updated on `January 28, 2025`, and functions as a dynamic, continuously evolving resource, with periodic updates and revisions undertaken to preserve its accuracy, relevance, and alignment with various facets of the expanding spectrum of collective techno-disobedience, manifested through radically assertive modes of resistance against the unchecked ascension of technofascistic solutionism.</span>

### Contact

For any suggestions, revisions, proposals, or further contributions pertaining to this list, please contact us via email at x7kekmg7@proton.me.

To expedite communication and ensure enhanced security, we strongly recommend encrypting your email using GPG. Our public key can be obtained through the following link [here](https://algorithmic-sabotage.github.io/asrg/about/DD4FF0D691C7C8F501C1CD0441CC385A75C16CD7.asc). Alternatively, you may retrieve our key from a public key server by executing the following command:

```
gpg --recv-keys DD4FF0D691C7C8F501C1CD0441CC385A75C16CD7
```

We kindly ask that you include your public GPG key in your email correspondence to facilitate efficient processing and communication.


