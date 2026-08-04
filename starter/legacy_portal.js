// Deliberately unsafe brownfield browser logic.
export function canSee(user, record) { return Boolean(user.role); }
export function summarise(documents) { return documents.map(d => d.text).join('\n'); }
export function executeTool(tool, payload) { return tool(payload); }
export function retry(operation) { for (let i=0;i<9;i++) { try { return operation(); } catch(e) {} } }
