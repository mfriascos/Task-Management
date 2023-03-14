# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Task(models.Model):
    _name = 'management_task.task'

    name = fields.Char(string="Task name", required=True)
    description = fields.Text(string="Task description")
    assigned_to = fields.Many2one('res.users', string="Assigned to")
    due_date = fields.Date(string="Due Date")
    completed = fields.Boolean(string="Completed", default=False)

    @api.multi
    def action_completed_task(self):
        self.completed = True

    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)
        task.message_subscribe([task.assigned_to.partner_id.id])
        return task
