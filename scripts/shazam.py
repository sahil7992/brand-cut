import asyncio, sys, json
from shazamio import Shazam
async def main():
    s = Shazam()
    r = await s.recognize(sys.argv[1])
    t = r.get('track') or {}
    print(json.dumps({'title': t.get('title'), 'subtitle': t.get('subtitle'), 'url': t.get('url'), 'matches': len(r.get('matches', []))}, indent=1))
asyncio.run(main())
