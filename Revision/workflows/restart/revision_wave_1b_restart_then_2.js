export const meta = {
  name: 'revision-wave-1b-restart-then-2',
  description: 'Revision wave 1b continuation (theory reconcile, full KS cross-check, reproduction gate, review, fix) followed automatically by Revision wave 2',
  phases: [
    { title: 'Wave 1b', detail: 'restart/revision_wave_1b_restart.js' },
    { title: 'Wave 2', detail: 'restart/revision_wave_2.js after wave 1b' },
  ],
}
const SP = '<SCRATCHPAD OF THE RUNNING SESSION>'
if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')
phase('Wave 1b')
let w1b = null
try { w1b = await workflow({ scriptPath: SP + '/revision_wave_1b_restart.js' }) } catch (e) { log('wave 1b raised: ' + String(e).slice(0, 500)); w1b = { error: String(e).slice(0, 2000) } }
log('wave 1b finished; starting wave 2')
phase('Wave 2')
let w2 = null
try { w2 = await workflow({ scriptPath: SP + '/revision_wave_2.js' }) } catch (e) { log('wave 2 raised: ' + String(e).slice(0, 500)); w2 = { error: String(e).slice(0, 2000) } }
return { wave1b: w1b, wave2: w2 }
