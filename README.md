# [NYT Room for debate](https://www.nytimes.com/roomfordebate/) data + crawler

Contains (almost) every NYT RFD articles since July 12, 2010. 

The crawler is built with [scrapy](https://scrapy.org/).

## Data Format
example document in [`nyt_rfd_raw.json`](nyt_rfd_raw.json)
```
{
  "debate_url": "https://www.nytimes.com/roomfordebate/2016/03/29/does-turkey-still-belong-in-nato",
  "debate_headline": "Does Turkey Still Belong in NATO?",
  "debate_date": "March 29, 2016",
  "debate_introduction": "Turkey is one of the oldest and most strategically located members of NATO. But when its president, Recep Tayyip Erdogan, visits Washington this week to attend the Nuclear Security Summit, he won’t be meeting with President Obama. That’s an indication of how his increasingly autocratic rule  has alienated his allies. There is no formal mechanism for NATO to expel a member, but given Erdogan’s record on human rights and how his focus on the rebellious Kurdish minority has interfered with his fight against ISIS, does Turkey still belong in the alliance?",
  "debate_articles": {
    "article_url": "https://www.nytimes.com/roomfordebate/2016/03/29/does-turkey-still-belong-in-nato/turkey-is-vital-to-nato-militarily",
    "author_description": "Can Kasapoglu is a defense analyst at the Center for Economics and Foreign Policy Studies in Istanbul. He was a visiting scholar at the NATO Defense College. ",
    "author_description_links": [
      "https://www.edam.org.tr/en/AnaKategori/research-team"
    ],
    "publication_date": "July 18, 2016,  3:59 PM",
    "headline": "Turkey Is Vital to NATO Militarily",
    "summary": "It shares the alliance's tactical nuclear burden, hosts crucial radar facilities and is to be a part of its most potent and reactive strike force.",
    "content": "Turkey’s membership in NATO is crucial as a matter of realpolitik and the weight it provides for the balance of military power. Under NATO’s nuclear burden-sharing agreement, Turkey hosts tactical nuclear weapons. This provides a bargaining chip to pressure Moscow to be more transparent about, and to reduce, its menacing non-strategic nuclear stocks. These tactical nuclear weapons also provide a deterrent against burgeoning chemical and biological warfare capacities of non-state actors in the Middle East. After the 2010 Lisbon Summit, Turkey agreed to host the crucial X-band radar in support of NATO’s ballistic missile defense efforts. The radar, which provides immediate data if there is a  ballistic missile threat, has become a primary asset of the NATO missile defense network’s sensor capabilities. This has become especially important since Iran managed to keep its growing ballistic missile capabilities out of its nuclear deal with the West.Turkey has also volunteered to be one of the key nations in what is the spearhead of the alliance’s force, the Very High Readiness Joint Task Force. The force, ready for deployment at very short notice, is the heart of NATO’s strategic vision of confronting threats. Given the Turkish armed forces’ elite special operations units, their expertise in low intensity conflicts, and their key role in the NATO response structure, Turkey’s contribution to the task force would be invaluable. This is augmented by the NATO Center of Excellence-Defense Against Terrorism in Ankara. By  helping head off possible threats from Russia, and confronting militants to its south, Turkey’s  military is a vital element of NATO defenses. NATO needs Turkey.                  "
  }
}
```
##
