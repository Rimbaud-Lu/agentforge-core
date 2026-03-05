import AgentStatus from '../components/AgentStatus'
import TaskMetrics from '../components/TaskMetrics'

export default function Home() {
  return (
    <div style={{padding: '40px', fontFamily: 'system-ui, sans-serif'}}>
      <h1>🤖 AgentForge Dashboard</h1>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginTop: '20px'}}>
        <AgentStatus />
        <TaskMetrics />
      </div>
    </div>
  )
}
