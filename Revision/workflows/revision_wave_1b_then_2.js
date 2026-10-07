export const meta = {
  name: 'revision-wave-1b-then-2',
  description: 'Revision wave 1b (repair, full Kohn-Sham cross-check, reproduction gate, skeptic review, fix) followed automatically by Revision wave 2 (dark sector, a4 with KS source, T3, documents, notebooks, gate, review, fix)',
  phases: [
    { title: 'Wave 1b', detail: 'revision_wave_1b.js as a sub-workflow' },
    { title: 'Wave 2', detail: 'revision_wave_2.js as a sub-workflow, after wave 1b' },
  ],
}
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad'
phase('Wave 1b')
let w1b = null
try {
  w1b = await workflow({ scriptPath: SP + '/revision_wave_1b.js' })
} catch (e) {
  log('wave 1b raised: ' + String(e).slice(0, 500))
  w1b = { error: String(e).slice(0, 2000) }
}
log('wave 1b finished; starting wave 2')
phase('Wave 2')
let w2 = null
try {
  w2 = await workflow({ scriptPath: SP + '/revision_wave_2.js' })
} catch (e) {
  log('wave 2 raised: ' + String(e).slice(0, 500))
  w2 = { error: String(e).slice(0, 2000) }
}
return { wave1b: w1b, wave2: w2 }
