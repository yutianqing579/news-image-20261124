[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yutianqing579/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/yutianqing579/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World Today — 24 November 2026 in one image

An entry for make.fun's bounty **“Sum up 24 November's world news in one image.”**

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. The image is a one-page newspaper front page that sums up
the world's news of Tuesday 24 November 2026:

- **Lead:** COP31 climate talks collapse with no deal — the EU and its allies
  reject a final text that dropped any mention of moving away from fossil fuels.
- **War at sea:** Ukraine's sea drones hit a Russian warship off Libya; the UN
  mission calls for an independent investigation into the Benghazi port attacks.
- **Also on the page:** NATO vows to counter the reported Russian nuclear-armed
  satellite threat · global landmine casualties hit a five-year high of 7,000 ·
  U.S. states sue Elon Musk's companies over sexualised images made with Grok ·
  the GTA VI hacker is sentenced to seven years in the UK but walks free ·
  Russian strikes kill at least 15 in the Kyiv region · Germany becomes the
  first country to gain access to Ukraine's Delta battle system · Israeli
  strikes kill six in Gaza · Armenia unveils a draft constitution.

Compiled from Reuters, BBC, UN News, SCMP and Kyiv Independent reports of
24 November 2026. `build_image.py` (Python + Pillow) is the generator that drew
`entry.png`; it is kept in the repository for transparency — the submitted
program itself is only the copy step, so grading runs are deterministic.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (1024×1024 PNG, under 1 MiB)
```

Licensed under the MIT License.
