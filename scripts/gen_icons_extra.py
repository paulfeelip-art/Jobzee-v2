# Extra service-family icons in the same style as the pack (24px, stroke 1.8, round caps).
import os
OUT = os.path.join(os.path.dirname(__file__), 'jobzee-design', 'project', 'assets', 'icons')
P = {
 'reparatii': '<path d="M14.5 6.5a4 4 0 0 0-5 5L4 17l3 3 5.5-5.5a4 4 0 0 0 5-5L15 12l-3-3z"/>',
 'tamplarie': '<path d="M6 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17M3 21h18"/><circle cx="14.5" cy="12" r="1"/>',
 'gresie': '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M12 3.5v17M3.5 12h17"/>',
 'clima': '<path d="M12 2v20M4.5 6.5l15 11M19.5 6.5l-15 11M9 4l3 2 3-2M9 20l3-2 3 2"/>',
 'lacatus': '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M21 12v2"/>',
 'auto': '<path d="M4 16v-3l2-5h12l2 5v3"/><path d="M3 16h18v3H3zM6.5 19v1.5M17.5 19v1.5"/><circle cx="7.5" cy="13.5" r=".6"/><circle cx="16.5" cy="13.5" r=".6"/>',
 'livrari': '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5M12 12v9M7.5 5.3l9 4.5"/>',
 'gatit': '<path d="M4 11h16v3a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6zM2 11h20M9 7c0-1 1-1.5 1-2.5M14 7c0-1 1-1.5 1-2.5"/>',
 'babysitting': '<circle cx="12" cy="9" r="5"/><path d="M10 8.5h.01M14 8.5h.01M10.5 11a2 2 0 0 0 3 0M7 21c.5-3 2.5-5 5-5s4.5 2 5 5"/>',
 'meditatii': '<path d="M3 5.5C5 4.5 8.5 4.5 12 6.5c3.5-2 7-2 9-1v13c-2-1-5.5-1-9 1-3.5-2-7-2-9-1zM12 6.5v13"/>',
 'evenimente': '<path d="M12 3a5 5 0 0 1 5 5c0 3.5-3 6-5 6s-5-2.5-5-6a5 5 0 0 1 5-5zM12 14l-1 2h2zM12 16c0 2-2 2.5-2 5"/>',
 'foto': '<path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="3.5"/>',
 'frumusete': '<circle cx="6" cy="7" r="3"/><circle cx="6" cy="17" r="3"/><path d="M8.5 8.5 20 18M8.5 15.5 20 6"/>',
 'fitness': '<path d="M6.5 6.5v11M17.5 6.5v11M3.5 9v6M20.5 9v6M6.5 12h11"/>',
 'calcat': '<path d="M3 17h17v-3a6 6 0 0 0-6-6H7l-1 3h8"/><path d="M3 17l1-5"/><path d="M8 20h8"/>',
 'dezinsectie': '<ellipse cx="12" cy="14" rx="4.5" ry="6"/><circle cx="12" cy="6" r="2"/><path d="M7.5 11 4 9.5M7.5 15H4M7.5 18.5 5 20.5M16.5 11l3.5-1.5M16.5 15H20M16.5 18.5l2.5 2M12 9v11"/>',
 'geamuri': '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M12 3v18M4 12h16M15 6l2 2"/>',
 'acte': '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 'toate': '<rect x="4" y="4" width="6.5" height="6.5" rx="2"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="2"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="2"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="3.25"/>',
}
for k, v in P.items():
    open(os.path.join(OUT, 'icon-%s.svg' % k), 'w').write('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FF8A00" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + v + '</svg>')
print(len(P))
